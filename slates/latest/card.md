# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T17:31:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +26.88 | +10.72 | +25.90 | 0.805 | -11.80 | -21.55 | 102.44 |
| B thesis-diversified (joint) ← optimiser card | 145.27 | +31.19 | +15.61 | +29.26 | 0.811 | -12.42 | -23.32 | 149.74 |
| C best expression per thesis | 148.71 | +30.09 | +14.62 | +27.30 | 0.747 | -22.32 | -35.12 | 136.96 |
| R FUNDED research stakes | 16.00 | +3.90 | +2.18 | +2.24 | 0.588 | -6.19 | -7.70 | 0.00 |

## SEA @ CAR  ·  10000 joint draws  ·  430 bet sides mapped, 47 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.760 / away 0.239

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_SEA_win | p_overtime | goals | shots CAR/SEA | CAR/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.187 | 0.65 | 0.35 | 0.00 | 6.06 | 34.7/20.7 | 17.9/30.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.152 | 0.54 | 0.46 | 0.45 | 5.95 | 34.6/20.8 | 17.6/31.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.147 | 0.65 | 0.35 | 0.00 | 9.44 | 36.6/22.2 | 17.3/28.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.077 | 0.61 | 0.39 | 0.00 | 3.46 | 33.5/19.7 | 18.2/31.2 | even strength |
| CAR shot control · high event (8+) · tight (1-goal/OT) | 0.070 | 0.54 | 0.46 | 0.59 | 9.61 | 36.7/22.7 | 17.1/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.069 | 0.57 | 0.43 | 0.00 | 6.07 | 27.7/26.5 | 23.2/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 13 | 0.224 | 0.199 | +0.086 | +0.061 | $4.29 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 42 | 0.639 | 0.493 | +0.202 | +0.057 | $2.34 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 55 | 0.759 | 0.620 | +0.192 | +0.052 | $5.73 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Kaapo Kakko: 1+ goals YES | 14 | 0.203 | 0.186 | +0.054 | +0.037 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: higher confidence-adjusted growth (65.55 vs 53.95 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.923 vs 0.516); relationships: KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.141); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26NOV14SEACAR-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (53.95 vs 28.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.296); relationships: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: DUPLICATIVE (phi 0.75); KXNHLGOAL-26NOV14SEACAR-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.142); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes; why: KXNHLSPREAD-26NOV14SEACAR-SEA3|yes has the higher standalone adjusted growth (53.95 vs 24.69 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.222); relationships: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLSPREAD-26NOV14SEACAR-CAR2|no: DUPLICATIVE (phi 0.75); KXNHLGOAL-26NOV14SEACAR-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.118); failure: CAR wins by 2+
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes has the higher standalone adjusted growth (65.55 vs 23.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26NOV14SEACAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLSPREAD-26NOV14SEACAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.118); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.15.
- thesis SEA:OFFENSE_4PLUS (p 0.3738): highest fidelity KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.223): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no (same contract)
- thesis CAR:SUPPRESSED (p 0.3053): highest fidelity KXNHLSPREAD-26NOV14SEACAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14SEACAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14SEACAR-SEABCATTON27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4139, phi -0.23)
- KXNHLSPREAD-26NOV14SEACAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 22.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3607, phi -1.0)
- KXNHLSPREAD-26NOV14SEACAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 21.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3607, phi -0.75)
- KXNHLGOAL-26NOV14SEACAR-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4139, phi -0.222)

portfolios: A EV +4.18 (adj +1.04) on $11.04, P(profit) 0.6856, adj growth 10.1 bp · B EV +6.62 (adj +3.38) on $14.94, P(profit) 0.7318, adj growth 32.3 bp · C EV +6.51 (adj +3.95) on $8.00, P(profit) 0.307, adj growth 36.8 bp · R EV +2.38 (adj +1.20) on $5.00, P(profit) 0.6918, adj growth 44.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV14SEACAR-CAR|no == KXNHLGAME-26NOV14SEACAR-SEA|yes

## WPG @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.407 / away 0.593

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.46 | 0.54 | 0.00 | 6.04 | 26.8/27.3 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.47 | 5.95 | 26.7/27.0 | 23.8/23.4 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.098 | 0.39 | 0.61 | 0.00 | 6.04 | 21.2/32.2 | 27.8/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.47 | 0.53 | 0.00 | 9.25 | 27.9/28.2 | 22.2/22.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.48 | 0.52 | 0.49 | 5.91 | 21.3/32.3 | 28.7/18.1 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.39 | 0.61 | 0.00 | 9.29 | 22.5/34.1 | 26.5/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.263 | 0.249 | +0.042 | +0.027 | $2.67 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Josh Morrissey: 1+ assists NO | 54 | 0.675 | 0.584 | +0.118 | +0.027 | $4.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 60 | 0.733 | 0.640 | +0.117 | +0.023 | $6.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Oliver Moore: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (9.12 vs 3.57 bp); despite a smaller raw edge (+0.042 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14WPGCHI-WPG2|no; why: higher confidence-adjusted growth (6.32 vs 3.57 bp); relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WPG offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14WPGCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (5.06 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: CHI offense succeeds (4+ goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.12 vs 3.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.367): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.3806): highest fidelity KXNHLSPREAD-26NOV14WPGCHI-WPG2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4142): highest fidelity KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26NOV14WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.244)
- KXNHLAST-26NOV14WPGCHI-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.0 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4042, phi -0.257)
- KXNHLAST-26NOV14WPGCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.367, phi -0.231)
- KXNHLGOAL-26NOV14WPGCHI-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4142, phi -0.172)

portfolios: A EV +1.53 (adj +0.37) on $11.04, P(profit) 0.7506, adj growth 3.6 bp · B EV +2.89 (adj +0.93) on $14.83, P(profit) 0.669, adj growth 8.9 bp · C EV +4.00 (adj +1.19) on $22.88, P(profit) 0.6341, adj growth 11.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 17 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MIN_win | p_overtime | goals | shots BOS/MIN | BOS/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.04 | 28.0/28.3 | 25.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.47 | 5.95 | 28.3/28.6 | 25.4/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.58 | 0.42 | 0.00 | 9.46 | 29.7/29.9 | 24.3/23.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.077 | 0.54 | 0.46 | 0.00 | 6.01 | 22.9/33.7 | 30.1/19.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.46 | 5.92 | 22.5/33.5 | 30.2/19.3 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.058 | 0.62 | 0.38 | 0.00 | 6.0 | 32.7/22.3 | 19.5/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 5 | 0.086 | 0.073 | +0.032 | +0.020 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 59 | 0.655 | 0.635 | +0.048 | +0.028 | $5.29 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Michael Eyssimont: 1+ goals YES | 12 | 0.153 | 0.144 | +0.026 | +0.016 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV14MINBOS-BOS5|yes; why: higher confidence-adjusted growth (16.04 vs 3.22 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.763 vs 0.534); relationships: KXNHLGOAL-26NOV14MINBOS-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26NOV14MINBOS-BOSMEYSSIMONT81-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN wins (incl. OT/SO)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14MINBOS-MIN2|no; why: higher confidence-adjusted growth (7.25 vs 2.51 bp); despite a smaller raw edge (+0.048 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26NOV14MINBOS-BOSMEYSSIMONT81-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense succeeds (4+ goals)
- **Michael Eyssimont: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV14MINBOS-BOS5|yes; why: higher confidence-adjusted growth (5.09 vs 3.22 bp); despite a smaller raw edge (+0.026 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.884 vs 0.534); relationships: KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14MINBOS-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BOS:WINS_BY_2PLUS (p 0.3217): highest fidelity KXNHLSPREAD-26NOV14MINBOS-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.403): highest fidelity KXNHLSPREAD-26NOV14MINBOS-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS (p 0.5426): highest fidelity KXNHLSPREAD-26NOV14MINBOS-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14MINBOS-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14MINBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:WINS (p 0.4574, phi -0.158)
- KXNHLGOAL-26NOV14MINBOS-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3729, phi -0.264)
- KXNHLGOAL-26NOV14MINBOS-BOSMEYSSIMONT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3484, phi -0.159)

portfolios: A EV +1.57 (adj +0.45) on $11.04, P(profit) 0.4519, adj growth 4.0 bp · B EV +1.44 (adj +0.87) on $7.83, P(profit) 0.7287, adj growth 8.3 bp · C EV +2.06 (adj +1.13) on $11.03, P(profit) 0.6798, adj growth 10.6 bp · R EV +0.16 (adj +0.09) on $2.00, P(profit) 0.655, adj growth 3.5 bp

## EDM @ TOR  ·  10000 joint draws  ·  446 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.428 / away 0.572

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_EDM_win | p_overtime | goals | shots TOR/EDM | TOR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.42 | 0.58 | 0.00 | 6.08 | 28.3/28.6 | 24.5/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.119 | 0.43 | 0.57 | 0.00 | 9.55 | 30.0/30.5 | 23.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.49 | 6.01 | 28.5/28.9 | 25.6/25.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.091 | 0.38 | 0.62 | 0.00 | 6.07 | 22.4/34.2 | 29.9/19.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.082 | 0.38 | 0.62 | 0.00 | 9.44 | 24.4/36.2 | 28.7/19.3 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.44 | 0.56 | 0.46 | 5.91 | 22.9/34.7 | 31.0/19.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.166 | 0.147 | +0.059 | +0.041 | $2.97 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 10 | 0.143 | 0.128 | +0.036 | +0.022 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 31 | 0.403 | 0.354 | +0.078 | +0.029 | $3.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.65) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 23 | 0.265 | 0.255 | +0.023 | +0.013 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (36.30 vs 1.37 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: TOR offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (10.81 vs 4.14 bp); despite a smaller raw edge (+0.036 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (8.44 vs 4.94 bp); despite a smaller raw edge (+0.078 vs +0.102/contract); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.181); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes; why: Player prop expression KXNHLGOAL-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.37 vs 0.46 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.181); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.408): highest fidelity KXNHLAST-26NOV14EDMTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3045): highest fidelity KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3755): highest fidelity KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14EDMTOR-TORJTAVARES91-1|no (same contract)
- KXNHLGOAL-26NOV14EDMTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3755, phi -0.213)
- KXNHLGOAL-26NOV14EDMTOR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3045, phi -0.149)
- KXNHLAST-26NOV14EDMTOR-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.488, phi -0.313)
- KXNHLGOAL-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3045, phi -0.209)
- override: Player prop expression KXNHLGOAL-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26NOV14EDMTOR-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.37 vs 0.46 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.99 (adj +0.62) on $11.04, P(profit) 0.6072, adj growth 6.0 bp · B EV +3.24 (adj +1.89) on $9.83, P(profit) 0.5762, adj growth 18.0 bp · C EV +5.20 (adj +2.62) on $20.34, P(profit) 0.5803, adj growth 24.4 bp · R EV +0.56 (adj +0.38) on $1.00, P(profit) 0.1657, adj growth 14.3 bp

## COL @ MTL  ·  10000 joint draws  ·  376 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_COL_win | p_overtime | goals | shots MTL/COL | MTL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.121 | 0.38 | 0.62 | 0.00 | 6.02 | 22.2/33.9 | 29.7/19.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.46 | 0.54 | 0.00 | 6.03 | 27.8/28.4 | 24.6/24.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.46 | 0.54 | 0.48 | 5.97 | 22.4/34.3 | 30.8/19.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.49 | 0.51 | 0.47 | 6.0 | 28.1/28.7 | 25.3/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.47 | 0.53 | 0.00 | 9.41 | 29.5/30.0 | 23.6/23.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.094 | 0.39 | 0.61 | 0.00 | 9.32 | 23.8/35.9 | 28.6/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Martin Necas: 1+ goals YES | 31 | 0.391 | 0.369 | +0.066 | +0.044 | $4.63 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 31 | 0.389 | 0.368 | +0.064 | +0.043 | $4.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
| Kirby Dach: 1+ goals YES | 13 | 0.158 | 0.150 | +0.020 | +0.012 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 50 | 0.615 | 0.534 | +0.098 | +0.016 | $2.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Martin Necas: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (19.41 vs 18.19 bp); relationships: KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14COLMTL-MTLKDACH77-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes has the higher standalone adjusted growth (19.41 vs 18.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV14COLMTL-MTLKDACH77-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: COL offense suppressed (<= 2 goals)
- **Kirby Dach: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14COLMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (2.59 vs 1.85 bp); despite a smaller raw edge (+0.020 vs +0.022/contract); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14COLMTL-COL3|yes; why: KXNHLSPREAD-26NOV14COLMTL-COL3|yes has the higher standalone adjusted growth (2.39 vs 2.35 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.148); relationships: KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV14COLMTL-MTLKDACH77-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4614): highest fidelity KXNHLTEAMTOTAL-26NOV14COLMTL-COL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:WINS_BY_2PLUS (p 0.3243): highest fidelity KXNHLSPREAD-26NOV14COLMTL-COL2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.385): highest fidelity KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV14COLMTL-COLMNECAS88-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3319, phi -0.287)
- KXNHLGOAL-26NOV14COLMTL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3319, phi -0.264)
- KXNHLGOAL-26NOV14COLMTL-MTLKDACH77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.385, phi -0.177)
- KXNHLAST-26NOV14COLMTL-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3971, phi -0.264)

portfolios: A EV +2.13 (adj +0.99) on $11.04, P(profit) 0.5989, adj growth 9.6 bp · B EV +2.44 (adj +1.39) on $12.64, P(profit) 0.6269, adj growth 13.3 bp · C EV +1.43 (adj +0.97) on $7.08, P(profit) 0.3907, adj growth 9.1 bp · R EV +0.40 (adj +0.27) on $2.00, P(profit) 0.3907, adj growth 10.2 bp

## DET @ TBL  ·  10000 joint draws  ·  370 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.654 / away 0.346

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.71 | 0.29 | 0.00 | 6.04 | 27.5/27.2 | 24.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.49 | 5.9 | 27.5/27.2 | 24.0/24.2 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.78 | 0.22 | 0.00 | 6.01 | 32.0/21.2 | 19.1/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.73 | 0.27 | 0.00 | 9.26 | 28.9/28.5 | 23.8/20.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.55 | 0.45 | 0.50 | 5.95 | 32.6/21.6 | 18.4/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.065 | 0.80 | 0.20 | 0.00 | 9.32 | 34.0/22.6 | 18.4/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jake Guentzel: 2+ goals YES | 8 | 0.114 | 0.105 | +0.029 | +0.019 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals YES | 38 | 0.445 | 0.426 | +0.048 | +0.029 | $3.35 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_STRONGER | D |
| Conor Geekie: 1+ goals NO | 83 | 0.873 | 0.861 | +0.033 | +0.021 | $5.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 37 | 0.463 | 0.414 | +0.077 | +0.028 | $3.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Jake Guentzel: 2+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes; why: higher confidence-adjusted growth (10.32 vs 7.87 bp); despite a smaller raw edge (+0.029 vs +0.048/contract); relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: DUPLICATIVE (phi 0.402); KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.201); failure: TBL offense suppressed (<= 2 goals)
- **Jake Guentzel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes has the higher standalone adjusted growth (10.32 vs 7.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.402); they share one thesis budget; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes: DUPLICATIVE (phi 0.402); KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.282); failure: TBL offense suppressed (<= 2 goals)
- **Conor Geekie: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (7.25 vs 7.10 bp); despite a smaller raw edge (+0.033 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (7.10 vs 0.75 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.201); KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.282); KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.5014): highest fidelity KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.2927): highest fidelity KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no (same contract)
- KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2927, phi -0.201)
- KXNHLGOAL-26NOV14DETTB-TBJGUENTZEL59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2927, phi -0.268)
- KXNHLGOAL-26NOV14DETTB-TBCGEEKIE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5014, phi -0.145)
- KXNHLAST-26NOV14DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5014, phi -0.307)

portfolios: A EV +1.61 (adj +0.85) on $11.04, P(profit) 0.7044, adj growth 8.2 bp · B EV +1.80 (adj +0.94) on $13.67, P(profit) 0.7044, adj growth 9.1 bp · C EV +2.13 (adj +1.04) on $8.82, P(profit) 0.5565, adj growth 9.8 bp · R EV +0.12 (adj +0.07) on $1.00, P(profit) 0.4445, adj growth 2.8 bp

## OTT @ PIT  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_OTT_win | p_overtime | goals | shots PIT/OTT | PIT/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.49 | 0.51 | 0.00 | 6.02 | 26.9/26.9 | 23.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.48 | 5.93 | 26.9/26.8 | 23.4/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.49 | 0.51 | 0.00 | 9.25 | 28.7/28.7 | 22.6/22.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.52 | 0.48 | 0.00 | 6.03 | 31.8/21.6 | 18.3/28.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.065 | 0.42 | 0.58 | 0.00 | 6.06 | 21.5/31.6 | 27.5/18.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.50 | 0.50 | 0.50 | 5.93 | 31.7/21.6 | 18.4/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Fabian Zetterlund: 1+ goals YES | 18 | 0.221 | 0.209 | +0.030 | +0.019 | $1.79 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.014 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 56 | 0.635 | 0.593 | +0.058 | +0.015 | $3.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14OTTPIT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (5.05 vs 0.70 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: OTT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14OTTPIT-OTT2|no; why: higher confidence-adjusted growth (3.91 vs 0.05 bp); despite a smaller raw edge (+0.025 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: PIT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV14OTTPIT-OTT2|no; why: higher confidence-adjusted growth (2.13 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:OFFENSE_4PLUS (p 0.3812): highest fidelity KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3918): highest fidelity KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3967): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV14OTTPIT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3918, phi -0.201)
- KXNHLGOAL-26NOV14OTTPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4032, phi -0.192)
- KXNHLAST-26NOV14OTTPIT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3967, phi -0.261)

portfolios: A EV +1.58 (adj +0.75) on $9.43, P(profit) 0.4015, adj growth 7.1 bp · B EV +0.82 (adj +0.39) on $6.00, P(profit) 0.3423, adj growth 3.7 bp · C EV +0.76 (adj +0.30) on $5.93, P(profit) 0.6876, adj growth 2.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ WSH  ·  10000 joint draws  ·  436 bet sides mapped, 7 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.452 / away 0.548

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.51 | 0.49 | 0.00 | 6.03 | 27.5/28.0 | 24.5/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.47 | 5.98 | 27.9/28.3 | 25.1/24.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.101 | 0.44 | 0.56 | 0.00 | 5.96 | 22.1/33.4 | 29.6/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.36 | 29.2/29.8 | 23.6/22.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.47 | 0.53 | 0.48 | 5.97 | 22.0/33.5 | 30.1/18.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 9.35 | 23.5/35.0 | 27.9/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cody Glass: 1+ goals YES | 10 | 0.151 | 0.133 | +0.045 | +0.027 | $2.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.230 | 0.214 | +0.040 | +0.024 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 15 | 0.188 | 0.174 | +0.029 | +0.015 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (16.48 vs 1.32 bp); relationships: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: NJD offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (7.80 vs 4.64 bp); despite a smaller raw edge (+0.040 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes has the higher standalone adjusted growth (7.80 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4072): highest fidelity KXNHLAST-26NOV14NJWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3763): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJNHISCHIER13-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4091): highest fidelity KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14NJWSH-NJAGRITSYUK81-1|yes (same contract)
- KXNHLGOAL-26NOV14NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3763, phi -0.178)
- KXNHLGOAL-26NOV14NJWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3824, phi -0.222)
- KXNHLGOAL-26NOV14NJWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3824, phi -0.189)

portfolios: A EV +3.06 (adj +1.47) on $11.04, P(profit) 0.6104, adj growth 13.7 bp · B EV +1.50 (adj +0.88) on $5.27, P(profit) 0.4703, adj growth 8.4 bp · C EV +0.98 (adj +0.56) on $10.20, P(profit) 0.362, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PHI_win | p_overtime | goals | shots CBJ/PHI | CBJ/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.56 | 0.44 | 0.00 | 5.97 | 26.7/26.4 | 23.2/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.82 | 26.5/26.2 | 23.1/23.3 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.093 | 0.64 | 0.36 | 0.00 | 5.9 | 31.7/20.8 | 18.1/27.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.54 | 0.46 | 0.49 | 5.84 | 32.1/21.2 | 18.0/28.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.072 | 0.54 | 0.46 | 0.00 | 3.45 | 25.5/25.2 | 23.4/23.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.52 | 0.48 | 0.48 | 2.75 | 25.1/24.9 | 23.6/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luca Del Bel Belluz: 1+ goals NO | 87 | 0.915 | 0.899 | +0.037 | +0.021 | $6.01 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 15 | 0.195 | 0.181 | +0.036 | +0.023 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.746 | 0.703 | +0.061 | +0.018 | $6.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Luca Del Bel Belluz: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14PHICBJ-CBJKJOHNSON91-1|no; why: higher confidence-adjusted growth (9.28 vs 1.79 bp); relationships: KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: CBJ offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14PHICBJ-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (8.27 vs 0.50 bp); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJLDELBELBELLUZ93-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14PHICBJ-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (3.18 vs 1.11 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14PHICBJ-CBJLDELBELBELLUZ93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.2828): highest fidelity KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.3166): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3556): highest fidelity KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14PHICBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26NOV14PHICBJ-CBJLDELBELBELLUZ93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3556, phi -0.125)
- KXNHLGOAL-26NOV14PHICBJ-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4947, phi -0.211)
- KXNHLAST-26NOV14PHICBJ-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.2828, phi -0.229)

portfolios: A EV +0.93 (adj +0.48) on $11.04, P(profit) 0.6862, adj growth 4.7 bp · B EV +1.30 (adj +0.61) on $14.23, P(profit) 0.7709, adj growth 5.9 bp · C EV +2.16 (adj +1.02) on $20.42, P(profit) 0.7127, adj growth 9.6 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.9154, adj growth 1.9 bp

## FLA @ STL  ·  10000 joint draws  ·  420 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.504 / away 0.496

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_FLA_win | p_overtime | goals | shots STL/FLA | STL/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 5.98 | 26.9/27.3 | 24.4/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.51 | 0.49 | 0.46 | 5.97 | 27.5/27.6 | 24.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.58 | 0.42 | 0.00 | 9.25 | 29.0/29.2 | 23.7/22.2 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.52 | 0.48 | 0.00 | 5.98 | 22.0/32.6 | 29.0/18.6 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 5.87 | 21.6/32.5 | 29.2/18.5 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.058 | 0.67 | 0.33 | 0.00 | 5.97 | 32.1/21.9 | 19.3/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 25 | 0.297 | 0.284 | +0.034 | +0.021 | $2.04 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 30 | 0.351 | 0.336 | +0.037 | +0.021 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.298 | 0.287 | +0.024 | +0.013 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (4.92 vs 4.60 bp); despite a smaller raw edge (+0.034 vs +0.037/contract); relationships: KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV14FLASTL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.92 vs 4.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV14FLASTL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: STL offense suppressed (<= 2 goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (4.92 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4304): highest fidelity KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes (same contract)
- thesis FLA:OFFENSE_4PLUS (p 0.348): highest fidelity KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASBENNETT9-1|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.4339): highest fidelity KXNHLGOAL-26NOV14FLASTL-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV14FLASTL-FLASREINHART13-1|no (same contract)
- KXNHLGOAL-26NOV14FLASTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3513, phi -0.256)
- KXNHLGOAL-26NOV14FLASTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3513, phi -0.266)
- KXNHLGOAL-26NOV14FLASTL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3513, phi -0.241)

portfolios: A EV +0.94 (adj +0.54) on $11.04, P(profit) 0.5512, adj growth 5.1 bp · B EV +0.65 (adj +0.38) on $5.66, P(profit) 0.5415, adj growth 3.7 bp · C EV +0.66 (adj +0.37) on $8.48, P(profit) 0.4274, adj growth 3.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ DAL  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BUF_win | p_overtime | goals | shots DAL/BUF | DAL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.02 | 26.5/26.5 | 23.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.46 | 5.93 | 26.5/26.5 | 23.2/23.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.67 | 0.33 | 0.00 | 5.97 | 31.3/21.1 | 18.5/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.58 | 0.42 | 0.00 | 9.26 | 28.1/27.9 | 22.4/21.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.57 | 0.43 | 0.49 | 5.88 | 31.6/21.4 | 18.2/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.57 | 0.43 | 0.00 | 3.46 | 25.2/25.3 | 23.6/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Olen Zellweger: 1+ goals YES | 6 | 0.088 | 0.080 | +0.025 | +0.016 | $1.18 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 15 | 0.196 | 0.182 | +0.037 | +0.023 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 13 | 0.166 | 0.154 | +0.028 | +0.017 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 28 | 0.326 | 0.313 | +0.032 | +0.019 | $2.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Olen Zellweger: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (9.22 vs 5.00 bp); despite a smaller raw edge (+0.024 vs +0.028/contract); relationships: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: BUF offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes; why: higher confidence-adjusted growth (8.54 vs 3.72 bp); relationships: KXNHLGOAL-26NOV14BUFDAL-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: DAL offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (5.00 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: BUF offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes has the higher standalone adjusted growth (8.54 vs 3.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV14BUFDAL-BUFOZELLWEGER8-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis DAL:OFFENSE_4PLUS (p 0.4165): highest fidelity KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.3328): highest fidelity KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes (same contract)
- KXNHLGOAL-26NOV14BUFDAL-BUFOZELLWEGER8-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4496, phi -0.148)
- KXNHLGOAL-26NOV14BUFDAL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3609, phi -0.217)
- KXNHLGOAL-26NOV14BUFDAL-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.4496, phi -0.214)
- KXNHLGOAL-26NOV14BUFDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3609, phi -0.257)

portfolios: A EV +1.75 (adj +1.09) on $8.13, P(profit) 0.5989, adj growth 10.3 bp · B EV +1.44 (adj +0.90) on $6.73, P(profit) 0.5989, adj growth 8.6 bp · C EV +1.14 (adj +0.69) on $5.16, P(profit) 0.3354, adj growth 6.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ UTA  ·  10000 joint draws  ·  398 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.636 / away 0.364

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_SJS_win | p_overtime | goals | shots UTA/SJS | UTA/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.65 | 0.35 | 0.00 | 6.05 | 28.0/27.5 | 24.7/23.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.113 | 0.69 | 0.31 | 0.00 | 6.06 | 33.2/22.0 | 19.3/28.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.47 | 5.89 | 28.1/27.6 | 24.4/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.70 | 0.30 | 0.00 | 9.43 | 29.6/29.1 | 24.0/22.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.57 | 0.43 | 0.45 | 5.92 | 33.2/22.1 | 19.0/29.9 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.079 | 0.72 | 0.28 | 0.00 | 9.34 | 35.6/23.5 | 19.0/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Daniil But: 1+ goals NO | 79 | 0.856 | 0.838 | +0.054 | +0.036 | $4.65 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Clayton Keller: 1+ assists NO | 39 | 0.472 | 0.429 | +0.066 | +0.022 | $1.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Vincent Trocheck: 1+ assists NO | 58 | 0.667 | 0.619 | +0.070 | +0.021 | $2.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 68 | 0.751 | 0.706 | +0.056 | +0.010 | $2.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Daniil But: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (18.62 vs 4.36 bp); despite a smaller raw edge (+0.054 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense succeeds (4+ goals)
- **Clayton Keller: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (4.36 vs 4.19 bp); despite a smaller raw edge (+0.066 vs +0.070/contract); relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.082); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: UTA offense succeeds (4+ goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no; why: second expression of the same thesis: KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no has the higher standalone adjusted growth (4.36 vs 4.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.082); they share one thesis budget; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi 0.082); KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV14SJUTA-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (1.10 vs 0.14 bp); despite a smaller raw edge (+0.056 vs +0.078/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:SUPPRESSED (p 0.3243): highest fidelity KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4652): highest fidelity KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no (same contract)
- KXNHLGOAL-26NOV14SJUTA-UTADBUT19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.164)
- KXNHLAST-26NOV14SJUTA-UTACKELLER9-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.325)
- KXNHLAST-26NOV14SJUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4757, phi -0.263)
- KXNHLAST-26NOV14SJUTA-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3148, phi -0.233)

portfolios: A EV +1.18 (adj +0.41) on $11.04, P(profit) 0.6351, adj growth 4.0 bp · B EV +1.13 (adj +0.44) on $11.84, P(profit) 0.6251, adj growth 4.3 bp · C EV +1.01 (adj +0.29) on $8.43, P(profit) 0.4722, adj growth 2.7 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.8558, adj growth 3.6 bp

## NYI @ ANA  ·  10000 joint draws  ·  440 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.510 / away 0.490

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NYI_win | p_overtime | goals | shots ANA/NYI | ANA/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 6.08 | 27.7/27.4 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 9.48 | 29.3/29.0 | 23.3/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.46 | 5.99 | 27.7/27.5 | 24.1/24.4 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.097 | 0.66 | 0.34 | 0.00 | 6.08 | 33.2/22.0 | 19.2/28.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.085 | 0.69 | 0.31 | 0.00 | 9.37 | 34.8/23.3 | 18.5/26.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.47 | 6.01 | 33.2/22.1 | 18.9/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Mintyukov: 1+ goals YES | 6 | 0.098 | 0.088 | +0.035 | +0.024 | $1.71 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.149 | 0.134 | +0.043 | +0.028 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Troy Terry: 1+ assists NO | 67 | 0.839 | 0.716 | +0.154 | +0.031 | $6.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Sam Colangelo: 1+ goals YES | 12 | 0.156 | 0.144 | +0.029 | +0.017 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (19.57 vs 3.17 bp); despite a smaller raw edge (+0.034 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.857 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (17.61 vs 3.17 bp); despite a smaller raw edge (+0.043 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.866 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: ANA offense suppressed (<= 2 goals)
- **Troy Terry: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV14NYIANA-ANACGAUTHIER61-1|no; why: higher confidence-adjusted growth (9.63 vs 0.01 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: ANA offense succeeds (4+ goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV14NYIANA-ANA2|yes; why: higher confidence-adjusted growth (5.68 vs 3.17 bp); despite a smaller raw edge (+0.029 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.503); relationships: KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5141): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [DIRECT], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3698): highest fidelity KXNHLSPREAD-26NOV14NYIANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.3931): highest fidelity KXNHLAST-26NOV14NYIANA-NYIMMACCELLI63-1|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV14NYIANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV14NYIANA-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.126)
- KXNHLGOAL-26NOV14NYIANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.136)
- KXNHLAST-26NOV14NYIANA-ANATTERRY19-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.9 pts; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.5141, phi -0.166)
- KXNHLGOAL-26NOV14NYIANA-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2867, phi -0.138)

portfolios: A EV +2.17 (adj +0.84) on $11.04, P(profit) 0.4354, adj growth 8.0 bp · B EV +3.50 (adj +1.68) on $11.44, P(profit) 0.3361, adj growth 16.1 bp · C EV +0.49 (adj +0.16) on $2.79, P(profit) 0.3698, adj growth 1.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ LAK  ·  10000 joint draws  ·  410 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_CGY_win | p_overtime | goals | shots LAK/CGY | LAK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.63 | 0.37 | 0.00 | 6.0 | 28.4/28.0 | 25.1/24.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 5.99 | 33.9/22.1 | 19.5/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.48 | 5.86 | 28.5/28.2 | 24.8/25.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.57 | 0.43 | 0.43 | 5.87 | 34.1/22.5 | 19.5/30.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 9.31 | 30.0/29.6 | 24.4/23.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.60 | 0.40 | 0.00 | 3.49 | 27.4/26.8 | 25.2/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kevin Fiala: 1+ assists NO | 61 | 0.819 | 0.673 | +0.192 | +0.047 | $5.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.078 | 0.071 | +0.024 | +0.017 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 65 | 0.701 | 0.686 | +0.035 | +0.020 | $3.68 | FUNDED_RESEARCH | $1 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Kevin Fiala: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (20.59 vs 6.47 bp); relationships: KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: LAK offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLPTS-26NOV14CGYLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (12.63 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no; why: KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (6.47 vs 4.00 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.035); relationships: KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3629): highest fidelity KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV14CGYLA-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3611): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:OFFENSE_4PLUS (p 0.2913): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV14CGYLA-LAKFIALA22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 22.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.191)
- KXNHLGOAL-26NOV14CGYLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3629, phi -0.137)
- KXNHLGOAL-26NOV14CGYLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4201, phi -0.228)

portfolios: A EV +2.25 (adj +0.82) on $11.04, P(profit) 0.5334, adj growth 7.9 bp · B EV +2.44 (adj +0.93) on $10.36, P(profit) 0.6243, adj growth 9.0 bp · C EV +1.56 (adj +0.33) on $9.15, P(profit) 0.8134, adj growth 3.2 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.7014, adj growth 1.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
