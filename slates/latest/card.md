# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T09:22:51Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.43 | +4.79 | +24.52 | 0.655 | -58.43 | -75.10 | 28.11 |
| B thesis-diversified (joint) ← optimiser card | 60.40 | +11.38 | +4.84 | +6.91 | 0.610 | -33.85 | -38.54 | 42.14 |
| C best expression per thesis | 54.34 | +8.22 | +2.71 | -1.23 | 0.492 | -27.80 | -27.80 | 24.03 |
| R FUNDED research stakes | 14.00 | +3.32 | +1.35 | -0.88 | 0.450 | -7.52 | -11.24 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  444 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.60 | 0.40 | 0.00 | 6.04 | 27.5/27.1 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.48 | 5.93 | 27.4/27.3 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.60 | 0.40 | 0.00 | 9.29 | 29.3/28.9 | 23.5/22.7 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.65 | 0.35 | 0.00 | 6.02 | 32.5/21.7 | 19.0/28.2 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.56 | 0.44 | 0.49 | 5.93 | 32.8/21.7 | 18.5/29.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 9.32 | 34.6/23.0 | 18.3/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 9 | 0.136 | 0.120 | +0.041 | +0.024 | $5.74 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Matty Beniers: 1+ goals YES | 19 | 0.230 | 0.217 | +0.029 | +0.017 | $4.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 15 | 0.186 | 0.173 | +0.027 | +0.015 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 21 | 0.248 | 0.235 | +0.027 | +0.013 | $4.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: higher confidence-adjusted growth (14.09 vs 4.12 bp); despite a smaller raw edge (+0.040 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT11SEAWSH-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Matty Beniers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no has the higher standalone adjusted growth (4.12 vs 3.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.158); relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT11SEAWSH-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no has the higher standalone adjusted growth (4.12 vs 3.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: SEA offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (2.23 vs 1.28 bp); despite a smaller raw edge (+0.027 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11SEAWSH-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.3515): highest fidelity KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4296): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2288): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.177)
- KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.214)
- KXNHLGOAL-26OCT11SEAWSH-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.208)
- KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3317, phi -0.215)

portfolios: A EV +8.70 (adj +1.70) on $50.00, P(profit) 0.5781, adj growth 10.8 bp · B EV +4.33 (adj +2.46) on $18.88, P(profit) 0.5945, adj growth 21.2 bp · C EV +2.35 (adj +0.88) on $20.87, P(profit) 0.7753, adj growth 7.7 bp · R EV +0.85 (adj +0.50) on $2.00, P(profit) 0.1362, adj growth 16.0 bp

## VAN @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.61 | 0.39 | 0.00 | 5.99 | 26.7/26.5 | 23.4/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.96 | 26.8/26.6 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.27 | 28.1/27.8 | 22.6/21.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.092 | 0.71 | 0.29 | 0.00 | 6.0 | 31.3/20.8 | 18.3/26.7 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.55 | 0.45 | 0.50 | 5.97 | 31.7/21.1 | 17.9/28.3 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.060 | 0.70 | 0.30 | 0.00 | 9.22 | 33.0/22.2 | 17.6/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver over 5.5 goals scored YES | 4 | 0.077 | 0.056 | +0.034 | +0.013 | $1.56 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.26) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 15 | 0.219 | 0.182 | +0.060 | +0.023 | $3.24 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York R wins by over 1.5 goals NO | 52 | 0.649 | 0.562 | +0.111 | +0.024 | $6.54 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 1.5 goals scored YES | 71 | 0.783 | 0.742 | +0.059 | +0.017 | $7.02 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.98) | EVIDENCE_MIXED | D |
- **Vancouver over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes; why: higher confidence-adjusted growth (9.03 vs 5.85 bp); despite a smaller raw edge (+0.034 vs +0.057/contract); relationships: KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.372); KXNHLSPREAD-26OCT11VANNYR-NYR2|no: REINFORCING (phi 0.205); KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.152); failure: NYR wins (incl. OT/SO)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes has the higher standalone adjusted growth (9.03 vs 8.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.372); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes: REINFORCING (phi 0.372); KXNHLSPREAD-26OCT11VANNYR-NYR2|no: DUPLICATIVE (phi 0.39); KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.279); failure: NYR wins (incl. OT/SO)
- **New York R wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes; why: higher confidence-adjusted growth (5.23 vs 3.31 bp); relationships: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes: REINFORCING (phi 0.205); KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: DUPLICATIVE (phi 0.39); KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.45); failure: NYR wins by 2+
- **Vancouver over 1.5 goals scored YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes has the higher standalone adjusted growth (9.03 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.152); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.279); KXNHLSPREAD-26OCT11VANNYR-NYR2|no: REINFORCING (phi 0.45); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2807): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes kept
- thesis VAN:WINS_BY_2PLUS (p 0.2194): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes: FUNDED_RESEARCH; family MIXED; loses 74% of the draws where the thesis happens; opposing: failure thesis NYR:WINS (p 0.5731, phi -0.299)
- KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS (p 0.5731, phi -0.614)
- KXNHLSPREAD-26OCT11VANNYR-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.4 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.3512, phi -1.0)
- KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis VAN:SUPPRESSED (p 0.4371, phi -0.597)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT11VANNYR-NYR3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes kept
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes kept

portfolios: A EV +11.24 (adj +1.70) on $50.00, P(profit) 0.5377, adj growth 8.0 bp · B EV +4.41 (adj +1.42) on $18.36, P(profit) 0.5977, adj growth 12.3 bp · C EV +3.98 (adj +1.14) on $13.47, P(profit) 0.6497, adj growth 9.9 bp · R EV +1.76 (adj +0.59) on $6.00, P(profit) 0.5977, adj growth 18.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.151 | 0.43 | 0.57 | 0.00 | 5.97 | 20.4/32.6 | 28.7/17.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.47 | 0.53 | 0.50 | 5.89 | 20.4/32.7 | 29.3/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.53 | 0.47 | 0.00 | 5.99 | 25.8/26.5 | 23.3/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.47 | 5.94 | 26.2/27.0 | 23.7/23.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.086 | 0.43 | 0.57 | 0.00 | 9.16 | 21.8/34.5 | 27.5/16.7 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.079 | 0.45 | 0.55 | 0.47 | 2.81 | 19.4/31.3 | 29.7/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 74 | 0.824 | 0.780 | +0.071 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 20 | 0.263 | 0.229 | +0.051 | +0.018 | $3.16 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes; why: higher confidence-adjusted growth (8.11 vs 4.04 bp); wins across more scripts (relative breadth 1.019 vs 0.55); relationships: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: REINFORCING (phi 0.276); failure: CAR wins by 2+
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (8.11 vs 4.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.276); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11CARPHI-CAR3|no: REINFORCING (phi 0.276); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:WINS (p 0.478): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.2626): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3491): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT11CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2868, phi -0.728)
- KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.522, phi -0.624)

portfolios: A EV +5.49 (adj +1.39) on $50.00, P(profit) 0.5513, adj growth 9.4 bp · B EV +2.65 (adj +0.96) on $23.16, P(profit) 0.8242, adj growth 8.7 bp · C EV +1.88 (adj +0.69) on $20.00, P(profit) 0.8242, adj growth 6.4 bp · R EV +0.71 (adj +0.26) on $6.00, P(profit) 0.8242, adj growth 9.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
