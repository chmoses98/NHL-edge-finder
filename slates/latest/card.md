# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T00:12:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.97 | +12.10 | +17.84 | 0.623 | -48.76 | -63.35 | 100.52 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +23.05 | +13.54 | +18.11 | 0.618 | -46.11 | -58.02 | 119.26 |
| C best expression per thesis | 99.75 | +13.37 | +5.68 | +13.86 | 0.644 | -29.26 | -42.21 | 51.02 |
| R FUNDED research stakes | 16.00 | +2.35 | +1.48 | -2.13 | 0.495 | -10.37 | -10.37 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  502 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.536 / away 0.464

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.07 | 27.3/27.4 | 24.0/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 6.0 | 27.6/27.6 | 24.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.59 | 0.41 | 0.00 | 9.39 | 28.7/28.7 | 23.0/22.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 6.06 | 31.9/21.7 | 18.9/27.5 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.51 | 0.49 | 0.00 | 6.05 | 21.7/32.1 | 28.4/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.47 | 5.96 | 32.5/22.0 | 18.9/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 88 | 0.910 | 0.901 | +0.023 | +0.014 | $19.36 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.014 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 26 | 0.303 | 0.291 | +0.029 | +0.017 | $5.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 17 | 0.206 | 0.195 | +0.026 | +0.015 | $4.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04OTTBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (4.31 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: BUF offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (3.34 vs 0.50 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04OTTBUF-BUFMSAMUELSSON23-1|yes; why: higher confidence-adjusted growth (3.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: BUF offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (3.34 vs 3.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3911): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4556): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3396): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04OTTBUF-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4556, phi -0.113)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3941, phi -0.19)
- KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3396, phi -0.254)
- KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3941, phi -0.182)

portfolios: A EV +3.00 (adj +1.77) on $35.27, P(profit) 0.5156, adj growth 14.8 bp · B EV +2.34 (adj +1.39) on $33.44, P(profit) 0.5156, adj growth 12.3 bp · C EV +1.26 (adj +0.76) on $10.14, P(profit) 0.4349, adj growth 6.6 bp · R EV +0.13 (adj +0.08) on $5.00, P(profit) 0.9101, adj growth 2.9 bp

## CHI @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.687 / away 0.313

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.134 | 0.72 | 0.28 | 0.00 | 6.03 | 32.7/20.8 | 18.4/27.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.56 | 0.44 | 0.47 | 5.9 | 32.9/21.0 | 18.0/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.64 | 0.36 | 0.00 | 6.08 | 27.0/26.3 | 23.4/22.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.096 | 0.72 | 0.28 | 0.00 | 9.25 | 34.6/22.5 | 18.0/26.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.52 | 0.48 | 0.48 | 5.93 | 27.1/26.5 | 23.3/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.63 | 0.37 | 0.00 | 9.26 | 28.6/27.8 | 22.6/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 59 | 0.675 | 0.653 | +0.069 | +0.046 | $19.31 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 10 | 0.146 | 0.133 | +0.040 | +0.027 | $6.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.267 | 0.252 | +0.045 | +0.030 | $9.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 53 | 0.626 | 0.560 | +0.079 | +0.013 | $12.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (19.45 vs 14.39 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV04CHIFLA-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: FLA offense succeeds (4+ goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (16.39 vs 11.20 bp); despite a smaller raw edge (+0.040 vs +0.045/contract); relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV04CHIFLA-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV04CHIFLA-FLA2|no; why: higher confidence-adjusted growth (11.20 vs 5.84 bp); despite a smaller raw edge (+0.045 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV04CHIFLA-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.187); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04CHIFLA-CHICBEDARD98-2|no; why: higher confidence-adjusted growth (1.47 vs 0.13 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.187); failure: CHI offense succeeds (4+ goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.13, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.3089): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3139): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4286): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV04CHIFLA-FLA2|no (same contract)
- KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4741, phi -0.242)
- KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.172)
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.256)
- KXNHLAST-26NOV04CHIFLA-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3139, phi -0.298)

portfolios: A EV +5.95 (adj +1.21) on $38.98, P(profit) 0.6467, adj growth 10.5 bp · B EV +8.54 (adj +4.82) on $48.40, P(profit) 0.6345, adj growth 42.5 bp · C EV +7.04 (adj +3.39) on $50.00, P(profit) 0.7108, adj growth 30.3 bp · R EV +0.56 (adj +0.38) on $5.00, P(profit) 0.6755, adj growth 13.9 bp

## SJS @ LAK  ·  10000 joint draws  ·  488 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.597 / away 0.403

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 5.98 | 27.9/27.4 | 24.4/23.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 6.0 | 33.4/22.2 | 19.5/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.9 | 28.1/27.8 | 24.6/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.59 | 0.41 | 0.51 | 5.83 | 33.2/22.2 | 19.2/29.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 9.23 | 29.3/28.8 | 23.8/22.4 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.064 | 0.71 | 0.29 | 0.00 | 9.13 | 34.7/22.9 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Macklin Celebrini: 2+ assists NO | 82 | 0.912 | 0.864 | +0.082 | +0.033 | $14.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 80 | 0.852 | 0.838 | +0.041 | +0.027 | $14.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.203 | 0.193 | +0.023 | +0.013 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Yaroslav Askarov: 28+ saves NO | 57 | 0.646 | 0.603 | +0.059 | +0.016 | $8.73 | FUNDED_RESEARCH | $3 | SJS:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Macklin Celebrini: 2+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (17.46 vs 4.06 bp); relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.046); KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: MOSTLY_INDEPENDENT (phi 0.016); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no; why: second expression of the same thesis: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no has the higher standalone adjusted growth (17.46 vs 10.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.108); they share one thesis budget; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: MOSTLY_INDEPENDENT (phi 0.015); failure: SJS offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04SJLA-SJMMISA77-1|yes; why: higher confidence-adjusted growth (2.64 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: MOSTLY_INDEPENDENT (phi -0.013); failure: SJS offense suppressed (<= 2 goals)
- **Yaroslav Askarov: 28+ saves NO** — thesis: SJS net faces light volume (<= 25 shots; LAK suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: SJS net faces heavy volume (33+ shots; LAK pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3045): highest fidelity KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes (same contract)
- thesis SJS:NET_LOW_VOLUME (p 0.3028): highest fidelity KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no (same contract)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.244)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.17)
- KXNHLGOAL-26NOV04SJLA-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4784, phi -0.21)
- KXNHLSAVE-26NOV04SJLA-SJYASKAROV30-28|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis SJS:NET_HIGH_VOLUME (p 0.2718, phi -0.705)

portfolios: A EV +7.28 (adj +1.32) on $38.98, P(profit) 0.6635, adj growth 11.6 bp · B EV +3.50 (adj +1.56) on $41.35, P(profit) 0.5953, adj growth 14.7 bp · C EV +5.07 (adj +1.53) on $39.61, P(profit) 0.6702, adj growth 14.1 bp · R EV +0.30 (adj +0.08) on $3.00, P(profit) 0.6463, adj growth 2.8 bp

## CGY @ SEA  ·  10000 joint draws  ·  446 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.64 | 0.36 | 0.00 | 6.03 | 28.2/28.4 | 25.5/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.44 | 5.86 | 28.4/28.3 | 25.2/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.67 | 0.34 | 0.00 | 9.45 | 29.9/30.0 | 24.9/22.5 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 6.09 | 22.9/34.1 | 30.8/19.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.068 | 0.70 | 0.30 | 0.00 | 6.0 | 33.2/22.8 | 20.3/28.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.058 | 0.51 | 0.49 | 0.50 | 5.92 | 23.0/34.0 | 30.7/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 11 | 0.170 | 0.153 | +0.053 | +0.037 | $8.85 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.162 | 0.146 | +0.045 | +0.029 | $7.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $6.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.205 | 0.194 | +0.025 | +0.014 | $3.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (27.52 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SEA offense suppressed (<= 2 goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (17.71 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (8.78 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: SEA offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (2.90 vs 0.72 bp); despite a smaller raw edge (+0.025 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4772): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.188)
- KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.177)

portfolios: A EV +11.74 (adj +7.80) on $36.77, P(profit) 0.4624, adj growth 63.5 bp · B EV +8.67 (adj +5.77) on $26.81, P(profit) 0.4624, adj growth 49.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +1.35 (adj +0.94) on $3.00, P(profit) 0.1696, adj growth 30.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
