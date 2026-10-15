# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T23:22:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +22.29 | +5.75 | +21.84 | 0.729 | -22.85 | -34.09 | 51.41 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +20.21 | +10.06 | +17.17 | 0.678 | -29.24 | -40.33 | 92.94 |
| C best expression per thesis | 150.00 | +20.09 | +8.45 | +17.33 | 0.671 | -34.48 | -48.74 | 74.97 |
| R FUNDED research stakes | 18.00 | +1.67 | +1.07 | +0.95 | 0.624 | -7.87 | -8.68 | 0.00 |

## PHI @ DET  ·  10000 joint draws  ·  438 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 5.93 | 27.1/26.6 | 23.2/23.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.115 | 0.56 | 0.44 | 0.00 | 5.96 | 32.8/21.2 | 18.1/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.85 | 27.4/26.9 | 23.7/24.2 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.53 | 0.47 | 0.48 | 5.88 | 32.6/21.4 | 18.2/29.1 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.53 | 0.47 | 0.50 | 2.8 | 30.8/20.0 | 18.7/29.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.50 | 2.83 | 26.1/25.7 | 24.2/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 82 | 0.887 | 0.869 | +0.057 | +0.039 | $13.04 | FUNDED_RESEARCH | $4 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 78 | 0.826 | 0.813 | +0.034 | +0.021 | $13.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.173 | 0.164 | +0.025 | +0.015 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 15 | 0.179 | 0.170 | +0.020 | +0.011 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15PHIDET-DETDLARKIN71-1|no; why: higher confidence-adjusted growth (23.83 vs 4.77 bp); relationships: KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: DET offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (5.96 vs 0.70 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.997 vs 0.344); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: PHI offense succeeds (4+ goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (4.01 vs 2.15 bp); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (2.15 vs 2.07 bp); despite a smaller raw edge (+0.020 vs +0.022/contract); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis DET:SUPPRESSED (p 0.4385): highest fidelity KXNHLTEAMTOTAL-26OCT15PHIDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15PHIDET-DETDLARKIN71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.328): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.4845): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15PHIDET-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.345, phi -0.161)
- KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.328, phi -0.177)
- KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4565, phi -0.187)
- KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4565, phi -0.236)

portfolios: A EV +1.73 (adj +0.64) on $25.00, P(profit) 0.6235, adj growth 5.9 bp · B EV +2.19 (adj +1.40) on $31.06, P(profit) 0.7766, adj growth 13.3 bp · C EV +1.49 (adj +0.77) on $25.11, P(profit) 0.6664, adj growth 6.9 bp · R EV +0.27 (adj +0.19) on $4.00, P(profit) 0.8871, adj growth 7.3 bp

## WPG @ CHI  ·  10000 joint draws  ·  472 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.0 | 26.4/26.6 | 23.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.91 | 26.4/26.7 | 23.4/23.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.097 | 0.45 | 0.55 | 0.00 | 5.96 | 21.1/31.9 | 28.0/17.9 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.50 | 0.50 | 0.49 | 5.92 | 21.2/31.8 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.49 | 0.51 | 0.00 | 9.32 | 28.0/28.2 | 22.1/21.9 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.059 | 0.43 | 0.57 | 0.00 | 9.15 | 22.4/33.5 | 26.4/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nino Niederreiter: 1+ assists NO | 79 | 0.875 | 0.830 | +0.073 | +0.028 | $12.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.314 | 0.299 | +0.040 | +0.025 | $5.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.792 | 0.777 | +0.039 | +0.023 | $12.27 | FUNDED_RESEARCH | $4 | CHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 26 | 0.298 | 0.287 | +0.024 | +0.014 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Nino Niederreiter: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no; why: higher confidence-adjusted growth (11.07 vs 0.05 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15WPGCHI-WPGGVILARDI13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: WPG offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15WPGCHI-CHIAVLASIC72-1|yes; why: higher confidence-adjusted growth (7.06 vs 0.01 bp); despite a smaller raw edge (+0.040 vs +0.070/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15WPGCHI-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CHI offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no; why: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15WPGCHI-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CHI offense succeeds (4+ goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-WPGAIAFALLO9-1|yes; why: higher confidence-adjusted growth (2.04 vs 1.35 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3726): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4051): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3743): highest fidelity KXNHLGOAL-26OCT15WPGCHI-WPGGVILARDI13-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-WPGGVILARDI13-1|yes (same contract)
- KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3743, phi -0.178)
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4051, phi -0.274)
- KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3726, phi -0.209)
- KXNHLGOAL-26OCT15WPGCHI-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4041, phi -0.258)
- override: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.95 (adj +0.81) on $25.00, P(profit) 0.7827, adj growth 7.7 bp · B EV +2.75 (adj +1.43) on $32.61, P(profit) 0.4395, adj growth 13.5 bp · C EV +2.42 (adj +1.48) on $30.01, P(profit) 0.4292, adj growth 13.2 bp · R EV +0.21 (adj +0.12) on $4.00, P(profit) 0.7922, adj growth 4.5 bp

## SJS @ NSH  ·  10000 joint draws  ·  466 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.542 / away 0.458

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.04 | 27.9/27.9 | 24.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 6.01 | 27.7/27.7 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.29 | 29.3/29.2 | 23.4/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.58 | 0.42 | 0.00 | 5.97 | 32.2/22.0 | 18.9/28.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.50 | 0.50 | 0.00 | 6.0 | 22.3/32.8 | 29.1/18.9 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.47 | 5.86 | 32.6/22.4 | 19.4/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ goals YES | 20 | 0.252 | 0.238 | +0.041 | +0.027 | $5.56 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 42 | 0.569 | 0.453 | +0.131 | +0.016 | $5.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.786 | 0.717 | +0.081 | +0.012 | $7.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (9.36 vs 0.71 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.37 vs 1.57 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: second expression of the same thesis: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no has the higher standalone adjusted growth (2.37 vs 1.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.044); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3851): highest fidelity KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3851, phi -0.221)
- KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.395, phi -0.274)
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.395, phi -0.204)

portfolios: A EV +5.12 (adj +1.30) on $25.00, P(profit) 0.6115, adj growth 11.5 bp · B EV +3.57 (adj +1.04) on $18.64, P(profit) 0.6115, adj growth 9.5 bp · C EV +3.81 (adj +1.27) on $15.39, P(profit) 0.6954, adj growth 11.2 bp · R EV +0.39 (adj +0.25) on $2.00, P(profit) 0.2524, adj growth 8.8 bp

## STL @ MIN  ·  10000 joint draws  ·  460 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.560 / away 0.440

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.58 | 0.42 | 0.00 | 6.04 | 27.7/27.4 | 23.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.46 | 5.99 | 27.7/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.58 | 0.42 | 0.00 | 9.3 | 29.3/29.1 | 23.3/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.9 | 19.2/28.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.53 | 0.47 | 0.48 | 5.93 | 32.7/22.1 | 18.9/29.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.21 | 34.7/23.4 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Hartman: 1+ goals YES | 18 | 0.232 | 0.218 | +0.042 | +0.028 | $5.67 | FUNDED_RESEARCH | $2 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.138 | 0.128 | +0.032 | +0.021 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 6 | 0.088 | 0.080 | +0.024 | +0.016 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 35 | 0.421 | 0.383 | +0.056 | +0.017 | $5.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.65) | EVIDENCE_MIXED | D |
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (10.71 vs 5.29 bp); despite a smaller raw edge (+0.042 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15STLMIN-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: MIN offense suppressed (<= 2 goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (10.71 vs 10.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15STLMIN-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.057); failure: MIN offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (8.88 vs 3.89 bp); despite a smaller raw edge (+0.024 vs +0.033/contract); relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no; why: higher confidence-adjusted growth (2.82 vs 2.25 bp); relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT15STLMIN-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3552): highest fidelity KXNHLAST-26OCT15STLMIN-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3426): highest fidelity KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.209)
- KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.153)
- KXNHLGOAL-26OCT15STLMIN-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4256, phi -0.143)
- KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4345, phi -0.317)

portfolios: A EV +4.09 (adj +1.22) on $25.00, P(profit) 0.6676, adj growth 10.6 bp · B EV +4.13 (adj +2.43) on $17.42, P(profit) 0.3978, adj growth 22.1 bp · C EV +3.90 (adj +2.09) on $38.66, P(profit) 0.6848, adj growth 18.6 bp · R EV +0.44 (adj +0.29) on $2.00, P(profit) 0.2323, adj growth 10.1 bp

## UTA @ EDM  ·  10000 joint draws  ·  472 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.01 | 27.6/27.5 | 24.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 9.48 | 29.4/29.4 | 24.0/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 6.03 | 28.0/27.8 | 24.5/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.07 | 32.5/22.0 | 19.3/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 9.5 | 34.3/23.3 | 18.6/26.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.55 | 0.45 | 0.47 | 5.97 | 32.8/22.2 | 19.1/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 16 | 0.216 | 0.200 | +0.047 | +0.030 | $5.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.127 | 0.116 | +0.032 | +0.020 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 65 | 0.703 | 0.689 | +0.037 | +0.023 | $11.26 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.489 | 0.447 | +0.062 | +0.020 | $6.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (13.85 vs 5.64 bp); despite a smaller raw edge (+0.047 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (13.85 vs 9.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: EDM offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no; why: Player prop expression KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: UTA offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (3.63 vs 3.45 bp); despite a smaller raw edge (+0.062 vs +0.098/contract); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.499): highest fidelity KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5762): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4009): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no — Player prop expression KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.201)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.135)
- KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3804, phi -0.249)
- KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.499, phi -0.307)
- override: Player prop expression KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.11 (adj +1.04) on $25.00, P(profit) 0.4691, adj growth 8.6 bp · B EV +4.20 (adj +2.36) on $26.62, P(profit) 0.5601, adj growth 21.5 bp · C EV +8.46 (adj +2.84) on $40.83, P(profit) 0.6871, adj growth 25.1 bp · R EV +0.17 (adj +0.10) on $3.00, P(profit) 0.7034, adj growth 3.8 bp

## CGY @ VGK  ·  10000 joint draws  ·  472 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.73 | 0.27 | 0.00 | 6.03 | 28.5/28.0 | 25.5/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.115 | 0.81 | 0.19 | 0.00 | 6.0 | 33.8/22.0 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.46 | 5.89 | 28.4/27.8 | 24.4/24.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.60 | 0.40 | 0.44 | 5.88 | 33.8/22.4 | 19.4/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 9.23 | 29.9/29.3 | 24.3/22.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.080 | 0.80 | 0.20 | 0.00 | 9.2 | 35.6/23.2 | 19.4/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.740 | 0.724 | +0.045 | +0.029 | $9.78 | FUNDED_RESEARCH | $3 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 64 | 0.777 | 0.685 | +0.120 | +0.028 | $9.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.085 | 0.077 | +0.021 | +0.014 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 16 | 0.190 | 0.180 | +0.021 | +0.011 | $1.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (8.45 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense succeeds (4+ goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (7.88 vs 0.76 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15CGYVGK-VGKBMCNABB3-1|yes; why: higher confidence-adjusted growth (6.56 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.054/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15CGYVGK-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (1.76 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:SUPPRESSED (p 0.2881): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VGK:OFFENSE_4PLUS (p 0.5061): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:OFFENSE_4PLUS (p 0.2554): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.21)
- KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.212)
- KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.107)
- KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5331, phi -0.219)

portfolios: A EV +2.29 (adj +0.74) on $25.00, P(profit) 0.6992, adj growth 7.1 bp · B EV +3.37 (adj +1.40) on $23.65, P(profit) 0.6799, adj growth 13.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.19 (adj +0.12) on $3.00, P(profit) 0.74, adj growth 4.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
