# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T04:08:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +22.08 | +4.10 | +19.80 | 0.683 | -66.24 | -82.02 | 22.56 |
| B thesis-diversified (joint) ← optimiser card | 50.99 | +8.88 | +3.04 | +4.84 | 0.631 | -22.21 | -29.19 | 26.82 |
| C best expression per thesis | 28.20 | +6.11 | +2.48 | -2.94 | 0.240 | -28.20 | -28.20 | 22.06 |
| R FUNDED research stakes | 17.00 | +2.87 | +0.94 | +2.68 | 0.643 | -8.03 | -10.03 | 0.00 |

## WPG @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_WPG_win | p_overtime | goals | shots DET/WPG | DET/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.57 | 0.43 | 0.00 | 5.99 | 27.3/27.2 | 24.0/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.52 | 0.48 | 0.47 | 5.89 | 27.2/27.0 | 23.6/23.8 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.086 | 0.60 | 0.40 | 0.00 | 5.97 | 32.3/21.6 | 18.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.57 | 0.43 | 0.00 | 9.19 | 28.8/28.8 | 23.2/22.4 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.53 | 0.47 | 0.48 | 5.81 | 32.1/21.6 | 18.5/28.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.55 | 0.45 | 0.00 | 3.45 | 26.1/25.9 | 24.2/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_UTA_win | p_overtime | goals | shots NYR/UTA | NYR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.56 | 0.44 | 0.00 | 6.02 | 26.4/26.6 | 23.4/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.98 | 26.3/26.6 | 23.3/22.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.46 | 0.54 | 0.00 | 6.05 | 21.1/31.9 | 28.1/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.56 | 0.44 | 0.00 | 9.25 | 27.7/28.0 | 22.3/21.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.47 | 0.53 | 0.44 | 5.9 | 21.1/31.8 | 28.4/18.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.055 | 0.47 | 0.53 | 0.00 | 9.17 | 22.2/33.2 | 26.8/16.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_FLA_win | p_overtime | goals | shots ANA/FLA | ANA/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.05 | 28.1/27.6 | 24.4/24.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.108 | 0.65 | 0.35 | 0.00 | 6.02 | 33.7/22.1 | 19.4/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.46 | 5.94 | 28.2/27.8 | 24.6/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.61 | 0.39 | 0.00 | 9.39 | 29.6/29.3 | 23.7/22.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.47 | 5.95 | 34.0/22.5 | 19.3/30.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 9.36 | 35.1/23.6 | 19.0/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 78 | 0.868 | 0.821 | +0.075 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 26 | 0.356 | 0.290 | +0.082 | +0.017 | $2.80 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 4.5 goals scored NO | 74 | 0.808 | 0.769 | +0.054 | +0.015 | $5.25 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Florida over 3.5 goals scored NO | 55 | 0.625 | 0.585 | +0.058 | +0.018 | $1.02 | FUNDED_RESEARCH | $1 | FLA:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-ANA3|yes; why: higher confidence-adjusted growth (11.50 vs 7.02 bp); wins across more scripts (relative breadth 1.035 vs 0.44); relationships: KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: REINFORCING (phi 0.29); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: REINFORCING (phi 0.49); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4|no: DUPLICATIVE (phi 0.453); failure: FLA wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: Broad expression KXNHLSPREAD-26OCT04FLAANA-ANA2|yes selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.29); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: DUPLICATIVE (phi 0.319); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4|no: REINFORCING (phi 0.434); failure: FLA wins (incl. OT/SO)
- **Florida over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT04FLAANA-FLA3|no has the higher standalone adjusted growth (11.50 vs 2.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.490); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: REINFORCING (phi 0.49); KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: DUPLICATIVE (phi 0.319); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4|no: DUPLICATIVE (phi 0.63); failure: FLA offense succeeds (4+ goals)
- **Florida over 3.5 goals scored NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04FLAANA-FLA3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4|no selected over broad KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT04FLAANA-FLA3|no: DUPLICATIVE (phi 0.453); KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: REINFORCING (phi 0.434); KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: DUPLICATIVE (phi 0.63); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:WINS (p 0.5767): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3556): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4217): highest fidelity KXNHLSPREAD-26OCT04FLAANA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04FLAANA-FLA3|no (same contract)
- KXNHLSPREAD-26OCT04FLAANA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2224, phi -0.731)
- KXNHLSPREAD-26OCT04FLAANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.1 pts; opposing: failure thesis FLA:WINS (p 0.4233, phi -0.636)
- KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3653, phi -0.643)
- KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3653, phi -0.979)
- override: Broad expression KXNHLSPREAD-26OCT04FLAANA-ANA2|yes selected over broad KXNHLSPREAD-26OCT04FLAANA-ANA3|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT04FLAANA-FLA2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5|no kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4|no selected over broad KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.69 (adj +1.87) on $50.00, P(profit) 0.5767, adj growth 10.8 bp · B EV +3.23 (adj +1.05) on $29.07, P(profit) 0.7743, adj growth 9.6 bp · C EV +1.91 (adj +0.74) on $20.00, P(profit) 0.8675, adj growth 7.0 bp · R EV +1.02 (adj +0.32) on $9.00, P(profit) 0.6494, adj growth 11.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04FLAANA-ANA|yes == KXNHLGAME-26OCT04FLAANA-FLA|no

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.60 | 0.40 | 0.00 | 5.99 | 28.3/28.2 | 25.0/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.9 | 28.1/28.1 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.64 | 0.36 | 0.00 | 9.26 | 29.7/29.9 | 24.7/22.6 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.68 | 0.32 | 0.00 | 5.99 | 33.4/22.3 | 19.7/28.8 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.45 | 5.82 | 33.3/22.9 | 19.9/29.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.64 | 0.36 | 0.00 | 3.44 | 27.0/26.9 | 25.5/24.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_VGK_win | p_overtime | goals | shots VAN/VGK | VAN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.45 | 0.55 | 0.00 | 5.99 | 27.1/27.6 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.47 | 5.98 | 27.2/27.6 | 24.4/23.8 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.103 | 0.38 | 0.62 | 0.00 | 6.05 | 21.1/32.5 | 28.3/18.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.50 | 0.50 | 0.48 | 5.93 | 21.6/32.9 | 29.6/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.47 | 0.53 | 0.00 | 9.38 | 28.2/28.9 | 22.4/22.2 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.072 | 0.35 | 0.65 | 0.00 | 9.3 | 22.9/34.5 | 26.8/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 15 | 0.240 | 0.193 | +0.082 | +0.034 | $7.12 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 1.5 goals NO | 55 | 0.682 | 0.593 | +0.115 | +0.026 | $1.60 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 68 | 0.794 | 0.717 | +0.099 | +0.022 | $8.80 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas over 4.5 goals scored NO | 68 | 0.761 | 0.715 | +0.065 | +0.020 | $4.39 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: higher confidence-adjusted growth (18.35 vs 10.40 bp); relationships: KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.384); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.286); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: REINFORCING (phi 0.289); failure: VGK wins (incl. OT/SO)
- **Vegas wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 5.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.384); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: DUPLICATIVE (phi 0.384); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: REINFORCING (phi 0.522); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 4.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.286); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: REINFORCING (phi 0.55); failure: VGK wins by 2+
- **Vegas over 4.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes has the higher standalone adjusted growth (18.35 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.289); they share one thesis budget; relationships: KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: REINFORCING (phi 0.289); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: REINFORCING (phi 0.522); KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: REINFORCING (phi 0.55); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2405): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4579): highest fidelity KXNHLSPREAD-26OCT04VGKVAN-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3643): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT04VGKVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS (p 0.5421, phi -0.612)
- KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.7 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3181, phi -1.0)
- KXNHLSPREAD-26OCT04VGKVAN-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3181, phi -0.745)
- KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4209, phi -0.658)

portfolios: A EV +12.39 (adj +2.23) on $50.00, P(profit) 0.5139, adj growth 11.7 bp · B EV +5.65 (adj +1.99) on $21.92, P(profit) 0.2405, adj growth 17.2 bp · C EV +4.21 (adj +1.74) on $8.20, P(profit) 0.2405, adj growth 15.1 bp · R EV +1.84 (adj +0.62) on $8.00, P(profit) 0.6272, adj growth 20.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
