# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T14:26:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.37 | +7.38 | +25.25 | 0.773 | -17.53 | -28.37 | 67.91 |
| B thesis-diversified (joint) ← optimiser card | 149.02 | +22.50 | +11.05 | +20.40 | 0.739 | -19.83 | -29.68 | 104.79 |
| C best expression per thesis | 150.00 | +26.77 | +9.91 | +24.51 | 0.720 | -28.25 | -41.08 | 89.52 |
| R FUNDED research stakes | 25.00 | +2.28 | +1.24 | +1.53 | 0.627 | -5.49 | -7.31 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  436 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 6.01 | 22.3/34.3 | 30.3/19.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.55 | 0.45 | 0.00 | 6.07 | 28.0/28.6 | 25.3/24.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.48 | 5.93 | 22.5/34.4 | 31.1/19.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.50 | 5.98 | 28.2/28.8 | 25.4/24.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 9.23 | 23.7/35.7 | 28.9/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.52 | 0.48 | 0.00 | 9.39 | 29.7/30.3 | 24.3/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 87 | 0.913 | 0.899 | +0.035 | +0.021 | $8.12 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (9.06 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BUF:SUPPRESSED (p 0.3784): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3988, phi -0.128)

portfolios: A EV +0.24 (adj +0.14) on $6.04, P(profit) 0.9134, adj growth 1.4 bp · B EV +0.33 (adj +0.19) on $8.12, P(profit) 0.9134, adj growth 1.9 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.9134, adj growth 2.8 bp

## NYI @ OTT  ·  10000 joint draws  ·  434 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.62 | 0.38 | 0.00 | 6.0 | 26.8/26.6 | 23.7/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.49 | 5.89 | 27.0/26.7 | 23.4/23.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 5.98 | 31.6/21.1 | 18.5/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 9.15 | 28.4/28.0 | 23.3/21.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.52 | 0.48 | 0.48 | 5.89 | 31.9/21.5 | 18.3/28.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.57 | 0.43 | 0.00 | 3.49 | 25.5/25.2 | 23.6/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 9 | 0.131 | 0.119 | +0.035 | +0.024 | $2.35 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ assists YES | 28 | 0.350 | 0.305 | +0.056 | +0.011 | $1.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-6|yes; why: higher confidence-adjusted growth (13.57 vs 1.04 bp); despite a smaller raw edge (+0.035 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.932 vs 0.691); relationships: KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NYI offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-6|yes; why: higher confidence-adjusted growth (1.21 vs 1.04 bp); wins across more scripts (relative breadth 0.917 vs 0.691); relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:OFFENSE_4PLUS (p 0.4218): highest fidelity KXNHLTOTAL-26OCT15NYIOTT-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT15NYIOTT-6|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3125): highest fidelity KXNHLTOTAL-26OCT15NYIOTT-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT15NYIOTT-6|yes (same contract)
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4683, phi -0.172)
- KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3635, phi -0.263)

portfolios: A EV +2.72 (adj +1.06) on $14.89, P(profit) 0.4342, adj growth 9.3 bp · B EV +1.10 (adj +0.62) on $3.65, P(profit) 0.4342, adj growth 5.9 bp · C EV +0.75 (adj +0.16) on $5.85, P(profit) 0.661, adj growth 1.5 bp · R EV +0.36 (adj +0.25) on $1.00, P(profit) 0.1306, adj growth 8.8 bp

## SEA @ TBL  ·  10000 joint draws  ·  408 bet sides mapped, 22 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.136 | 0.68 | 0.32 | 0.00 | 5.97 | 32.7/21.1 | 18.4/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.61 | 0.39 | 0.00 | 6.04 | 27.3/26.5 | 23.5/23.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.56 | 0.44 | 0.48 | 5.9 | 33.0/21.1 | 18.0/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.44 | 5.88 | 27.5/26.7 | 23.4/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.079 | 0.70 | 0.30 | 0.00 | 9.2 | 34.6/22.5 | 18.0/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.067 | 0.59 | 0.41 | 0.00 | 9.19 | 29.0/28.2 | 22.8/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 9 | 0.126 | 0.116 | +0.031 | +0.020 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 67 | 0.763 | 0.714 | +0.077 | +0.028 | $7.26 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ben Meyers: 1+ goals YES | 8 | 0.120 | 0.102 | +0.035 | +0.017 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.645 | 0.630 | +0.038 | +0.023 | $4.65 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: higher confidence-adjusted growth (10.13 vs 8.24 bp); despite a smaller raw edge (+0.031 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: SEA offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no; why: higher confidence-adjusted growth (8.24 vs 6.62 bp); wins across more scripts (relative breadth 1.015 vs 0.898); relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.204); failure: TBL wins by 2+
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15SEATB-TB3|no has the higher standalone adjusted growth (8.24 vs 8.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.071); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.204); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3554): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.303): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.427): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4793, phi -0.193)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3566, phi -0.749)
- KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4793, phi -0.144)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4314, phi -0.285)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.50 (adj +0.61) on $15.10, P(profit) 0.6978, adj growth 5.3 bp · B EV +2.33 (adj +1.18) on $15.32, P(profit) 0.6269, adj growth 11.2 bp · C EV +1.73 (adj +0.63) on $15.30, P(profit) 0.7628, adj growth 5.9 bp · R EV +0.35 (adj +0.16) on $4.00, P(profit) 0.5337, adj growth 6.0 bp

## VAN @ FLA  ·  10000 joint draws  ·  394 bet sides mapped, 23 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.116 | 0.64 | 0.36 | 0.00 | 6.03 | 32.6/21.2 | 18.5/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 6.03 | 27.3/26.7 | 23.6/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.45 | 5.92 | 27.6/27.0 | 23.7/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.46 | 5.93 | 32.8/21.5 | 18.4/29.2 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.087 | 0.70 | 0.30 | 0.00 | 9.22 | 34.2/22.6 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.60 | 0.40 | 0.00 | 9.27 | 28.7/28.3 | 22.7/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 12 | 0.187 | 0.169 | +0.060 | +0.042 | $4.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 15 | 0.219 | 0.199 | +0.060 | +0.040 | $4.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 62 | 0.703 | 0.680 | +0.066 | +0.043 | $8.12 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.237 | 0.219 | +0.046 | +0.029 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: higher confidence-adjusted growth (33.35 vs 25.92 bp); despite a smaller raw edge (+0.060 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.939 vs 0.563); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 25.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.181); relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (20.14 vs 17.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.144); relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: FLA offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 11.39 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.201); relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3508): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2178): highest fidelity KXNHLSPREAD-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2889): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.2)
- KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.202)
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4545, phi -0.233)
- KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.231)

portfolios: A EV +4.70 (adj +0.93) on $15.10, P(profit) 0.5387, adj growth 8.4 bp · B EV +5.32 (adj +3.56) on $20.09, P(profit) 0.4733, adj growth 33.7 bp · C EV +6.78 (adj +2.46) on $18.38, P(profit) 0.2866, adj growth 22.0 bp · R EV +0.31 (adj +0.20) on $3.00, P(profit) 0.7029, adj growth 7.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.128 | 0.55 | 0.45 | 0.00 | 5.94 | 33.2/21.1 | 17.9/29.1 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.55 | 0.45 | 0.47 | 5.89 | 32.9/21.3 | 18.1/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 6.0 | 27.4/26.7 | 23.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.47 | 5.85 | 27.3/26.7 | 23.6/24.0 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.074 | 0.56 | 0.44 | 0.00 | 9.15 | 34.5/22.6 | 17.5/27.6 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.068 | 0.55 | 0.45 | 0.00 | 3.52 | 31.7/20.1 | 18.4/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Matt Rempe: 1+ goals YES | 6 | 0.090 | 0.081 | +0.026 | +0.017 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.673 | 0.656 | +0.046 | +0.029 | $7.58 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.164 | 0.153 | +0.026 | +0.015 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 77 | 0.825 | 0.795 | +0.042 | +0.012 | $4.75 | FUNDED_RESEARCH | $2 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (10.53 vs 5.15 bp); despite a smaller raw edge (+0.026 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.072); failure: NYR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: higher confidence-adjusted growth (8.00 vs 4.66 bp); despite a smaller raw edge (+0.046 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: REINFORCING (phi 0.154); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NJDHAMILTON7-2|yes; why: higher confidence-adjusted growth (4.02 vs 0.12 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.812); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: INTENTIONAL_DIVERSIFIER (phi -0.129); failure: NJD offense suppressed (<= 2 goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ3|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.98 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.154); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.129); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4104): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3526): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ3|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.98 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:WINS (p 0.4878): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4239, phi -0.142)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3642, phi -0.26)
- KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4104, phi -0.186)
- KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2792, phi -0.741)
- override: Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ3|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.98 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.64 (adj +0.61) on $15.10, P(profit) 0.6535, adj growth 5.8 bp · B EV +1.79 (adj +1.05) on $15.65, P(profit) 0.6713, adj growth 9.9 bp · C EV +3.06 (adj +1.30) on $30.61, P(profit) 0.6638, adj growth 11.7 bp · R EV +0.26 (adj +0.12) on $4.00, P(profit) 0.5822, adj growth 4.7 bp

## PHI @ DET  ·  10000 joint draws  ·  404 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.54 | 0.46 | 0.00 | 5.93 | 32.3/21.1 | 18.0/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.50 | 0.50 | 0.00 | 5.96 | 27.2/26.8 | 23.3/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.84 | 32.9/21.3 | 18.2/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.49 | 5.89 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 3.44 | 26.3/25.6 | 23.8/24.5 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.77 | 31.2/20.3 | 18.8/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Nate Danielson: 1+ goals NO | 85 | 0.884 | 0.870 | +0.025 | +0.011 | $8.12 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.173 | 0.160 | +0.025 | +0.012 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 66 | 0.729 | 0.690 | +0.053 | +0.014 | $4.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes; why: higher confidence-adjusted growth (5.49 vs 2.32 bp); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: PHI offense suppressed (<= 2 goals)
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (2.41 vs 1.90 bp); despite a smaller raw edge (+0.025 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.118); failure: DET offense succeeds (4+ goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (5.49 vs 2.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (1.90 vs 0.78 bp); wins across more scripts (relative breadth 0.995 vs 0.35); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.118); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no (same contract)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)
- KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.163)
- KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.216)
- KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.227)

portfolios: A EV +1.32 (adj +0.59) on $15.10, P(profit) 0.3504, adj growth 5.6 bp · B EV +1.17 (adj +0.54) on $15.95, P(profit) 0.3408, adj growth 5.1 bp · C EV +1.44 (adj +0.65) on $13.49, P(profit) 0.2329, adj growth 5.8 bp · R EV +0.09 (adj +0.04) on $3.00, P(profit) 0.8839, adj growth 1.5 bp

## WPG @ CHI  ·  10000 joint draws  ·  416 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.50 | 0.50 | 0.00 | 6.0 | 26.6/27.0 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.87 | 26.3/26.6 | 23.4/23.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.096 | 0.44 | 0.56 | 0.00 | 6.01 | 21.0/31.9 | 27.8/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.48 | 0.52 | 0.46 | 5.91 | 21.3/32.0 | 28.5/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.36 | 27.8/28.2 | 21.8/21.8 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.23 | 22.3/33.4 | 25.9/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.176 | 0.157 | +0.049 | +0.030 | $3.28 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 52 | 0.660 | 0.563 | +0.123 | +0.025 | $7.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 28 | 0.321 | 0.308 | +0.026 | +0.014 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 22 | 0.253 | 0.242 | +0.021 | +0.010 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (17.20 vs 1.99 bp); relationships: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.094); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15WPGCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (5.59 vs 2.31 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.094); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.147); KXNHLGOAL-26OCT15WPGCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (17.20 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.147); KXNHLGOAL-26OCT15WPGCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (17.20 vs 1.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3693): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4146): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.4): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.203)
- KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3693, phi -0.256)
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.264)
- KXNHLGOAL-26OCT15WPGCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.237)

portfolios: A EV +2.89 (adj +1.21) on $15.10, P(profit) 0.3287, adj growth 11.5 bp · B EV +3.34 (adj +1.30) on $14.77, P(profit) 0.425, adj growth 12.3 bp · C EV +5.30 (adj +2.05) on $18.94, P(profit) 0.7373, adj growth 18.3 bp · R EV +0.38 (adj +0.23) on $1.00, P(profit) 0.1764, adj growth 8.7 bp

## SJS @ NSH  ·  10000 joint draws  ·  456 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 27.6/27.8 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.45 | 5.99 | 27.9/27.9 | 24.4/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 9.29 | 28.9/28.8 | 23.1/22.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 6.0 | 22.1/32.7 | 28.7/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.067 | 0.60 | 0.40 | 0.00 | 6.02 | 32.7/22.1 | 19.1/28.3 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.47 | 5.87 | 32.5/22.1 | 18.9/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 2+ assists NO | 93 | 0.980 | 0.952 | +0.045 | +0.018 | $7.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 13 | 0.173 | 0.160 | +0.035 | +0.022 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 80 | 0.834 | 0.823 | +0.022 | +0.011 | $5.85 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.798 | 0.718 | +0.093 | +0.013 | $4.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: REINFORCING (phi 0.288); failure: SJS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (8.58 vs 1.24 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (1.90 vs 0.16 bp); despite a smaller raw edge (+0.022 vs +0.114/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (1.82 vs 0.16 bp); despite a smaller raw edge (+0.093 vs +0.114/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: REINFORCING (phi 0.288); KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3847): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.121)
- KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3847, phi -0.192)
- KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.198)
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.196)

portfolios: A EV +1.45 (adj +0.57) on $15.10, P(profit) 0.7289, adj growth 5.4 bp · B EV +1.71 (adj +0.66) on $20.31, P(profit) 0.7283, adj growth 6.3 bp · C EV +1.88 (adj +1.00) on $19.81, P(profit) 0.1729, adj growth 9.2 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8336, adj growth 1.1 bp

## STL @ MIN  ·  10000 joint draws  ·  430 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 27.7/27.4 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.96 | 27.9/27.5 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.57 | 0.43 | 0.00 | 9.35 | 29.4/29.3 | 23.5/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.65 | 0.35 | 0.00 | 6.0 | 32.7/21.9 | 19.1/28.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.45 | 5.96 | 33.3/22.4 | 19.2/29.7 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 9.35 | 34.5/23.4 | 18.3/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Hartman: 1+ assists YES | 24 | 0.309 | 0.269 | +0.056 | +0.017 | $2.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.269 | 0.255 | +0.026 | +0.013 | $1.73 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.15 vs 0.70 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: MIN offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15STLMIN-STL5|yes; why: higher confidence-adjusted growth (2.01 vs 0.45 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.908 vs 0.537); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3598): highest fidelity KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes (same contract)
- KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.261)
- KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4272, phi -0.261)

portfolios: A EV +1.53 (adj +0.51) on $8.28, P(profit) 0.4993, adj growth 4.5 bp · B EV +0.65 (adj +0.23) on $3.82, P(profit) 0.4993, adj growth 2.2 bp · C EV +1.23 (adj +0.43) on $7.19, P(profit) 0.4993, adj growth 3.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.63 | 0.37 | 0.00 | 6.07 | 27.5/27.5 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.46 | 29.4/29.3 | 23.8/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.45 | 6.07 | 28.1/28.0 | 24.7/24.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.67 | 0.33 | 0.00 | 6.07 | 32.8/22.1 | 19.4/28.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.69 | 0.31 | 0.00 | 9.48 | 34.3/23.4 | 18.9/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.56 | 0.44 | 0.45 | 5.94 | 32.9/22.3 | 19.2/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor McDavid: 1+ assists NO | 32 | 0.452 | 0.363 | +0.117 | +0.028 | $4.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.129 | 0.113 | +0.033 | +0.017 | $1.88 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 17 | 0.217 | 0.201 | +0.037 | +0.021 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 69 | 0.798 | 0.718 | +0.093 | +0.013 | $5.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.49 vs 0.06 bp); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (7.46 vs 1.59 bp); despite a smaller raw edge (+0.033 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (6.76 vs 1.59 bp); despite a smaller raw edge (+0.037 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: EDM offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (1.85 vs 0.13 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2932): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4964): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3988): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4964, phi -0.318)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.154)
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.19)
- KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3865, phi -0.19)

portfolios: A EV +3.58 (adj +0.68) on $15.10, P(profit) 0.7171, adj growth 6.4 bp · B EV +3.51 (adj +1.13) on $14.69, P(profit) 0.5843, adj growth 10.7 bp · C EV +3.28 (adj +0.77) on $11.30, P(profit) 0.6709, adj growth 7.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ VGK  ·  10000 joint draws  ·  412 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.127 | 0.79 | 0.21 | 0.00 | 5.97 | 33.9/22.1 | 19.9/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.73 | 0.27 | 0.00 | 6.01 | 28.3/27.8 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.56 | 0.44 | 0.47 | 5.92 | 28.5/28.3 | 24.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.58 | 0.42 | 0.46 | 5.83 | 33.7/22.2 | 18.9/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.75 | 0.25 | 0.00 | 9.18 | 29.7/29.2 | 24.6/21.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.078 | 0.78 | 0.22 | 0.00 | 9.16 | 35.4/23.4 | 19.3/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Trevor Connelly: 1+ goals NO | 73 | 0.781 | 0.766 | +0.038 | +0.022 | $7.23 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Vegas wins by over 1.5 goals NO | 47 | 0.559 | 0.512 | +0.071 | +0.024 | $2.72 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Eichel: 1+ goals NO | 62 | 0.675 | 0.659 | +0.039 | +0.023 | $4.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $1.75 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: higher confidence-adjusted growth (5.72 vs 5.20 bp); despite a smaller raw edge (+0.038 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.85); relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.134); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (5.20 vs 4.11 bp); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: REINFORCING (phi 0.16); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (5.20 vs 4.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.160); they share one thesis budget; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: REINFORCING (phi 0.16); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.142); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (5.20 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: DUPLICATIVE (phi 0.754); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.142); failure: VGK wins by 2+

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no (same contract)
- KXNHLGOAL-26OCT15CGYVGK-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.195)
- KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -1.0)
- KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.235)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)

portfolios: A EV +1.78 (adj +0.47) on $15.10, P(profit) 0.6129, adj growth 4.3 bp · B EV +1.24 (adj +0.59) on $16.65, P(profit) 0.6468, adj growth 5.6 bp · C EV +1.33 (adj +0.46) on $9.13, P(profit) 0.5586, adj growth 4.1 bp · R EV +0.35 (adj +0.14) on $4.00, P(profit) 0.565, adj growth 5.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
