# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T01:31:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +21.42 | +5.64 | +28.37 | 0.631 | -46.69 | -64.42 | 43.09 |
| B thesis-diversified (joint) ← optimiser card | 97.17 | +10.98 | +5.14 | +8.26 | 0.601 | -32.58 | -45.74 | 45.28 |
| C best expression per thesis | 72.63 | +15.40 | +8.69 | +3.88 | 0.616 | -42.60 | -50.78 | 74.42 |
| R FUNDED research stakes | 14.00 | +1.84 | +0.68 | +2.17 | 0.673 | -6.49 | -8.08 | 0.00 |

## NYR @ VAN  ·  10000 joint draws  ·  416 bet sides mapped, 36 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.348 / away 0.652

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_NYR_win | p_overtime | goals | shots VAN/NYR | VAN/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.51 | 0.49 | 0.00 | 5.98 | 26.5/26.8 | 23.3/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.45 | 5.84 | 26.6/26.7 | 23.5/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.49 | 0.51 | 0.00 | 9.33 | 28.1/28.4 | 22.2/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.085 | 0.46 | 0.54 | 0.00 | 6.0 | 21.1/31.6 | 27.7/17.8 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.49 | 0.51 | 0.46 | 5.94 | 21.4/32.1 | 28.8/18.1 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.058 | 0.42 | 0.58 | 0.00 | 9.27 | 22.6/33.5 | 26.1/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 1.5 goals NO | 56 | 0.722 | 0.613 | +0.145 | +0.036 | $18.59 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mika Zibanejad: 1+ goals NO | 66 | 0.717 | 0.702 | +0.042 | +0.026 | $14.46 | FUNDED_RESEARCH | $4 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ goals NO | 71 | 0.764 | 0.748 | +0.040 | +0.024 | $15.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **New York R wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (29.85 vs 11.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.287); relationships: KXNHLGOAL-26NOV13NYRVAN-NYRMZIBANEJAD93-1|no: REINFORCING (phi 0.169); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: REINFORCING (phi 0.166); failure: NYR wins by 2+
- **Mika Zibanejad: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (29.85 vs 6.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.169); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense succeeds (4+ goals)
- **Gabe Perreault: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: Player prop expression KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no selected over player prop KXNHLAST-26NOV13NYRVAN-NYRPDOROFEYEV16-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.166); KXNHLGOAL-26NOV13NYRVAN-NYRMZIBANEJAD93-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3913): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2844): highest fidelity KXNHLSPREAD-26NOV13NYRVAN-NYR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3994): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV13NYRVAN-NYR2|no — Player prop expression KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no selected over player prop KXNHLAST-26NOV13NYRVAN-NYRPDOROFEYEV16-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.7 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.278, phi -1.0)
- KXNHLGOAL-26NOV13NYRVAN-NYRMZIBANEJAD93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.243)
- KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.22)
- override: Player prop expression KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no selected over player prop KXNHLAST-26NOV13NYRVAN-NYRPDOROFEYEV16-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +15.96 (adj +3.62) on $50.00, P(profit) 0.6233, adj growth 25.8 bp · B EV +6.40 (adj +2.23) on $48.59, P(profit) 0.6889, adj growth 19.9 bp · C EV +12.39 (adj +6.82) on $30.01, P(profit) 0.3017, adj growth 58.0 bp · R EV +1.50 (adj +0.47) on $9.00, P(profit) 0.5519, adj growth 16.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV13NYRVAN-NYR|no == KXNHLGAME-26NOV13NYRVAN-VAN|yes

## NSH @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NSH_win | p_overtime | goals | shots VGK/NSH | VGK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.124 | 0.73 | 0.27 | 0.00 | 5.99 | 33.4/21.6 | 19.1/28.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.64 | 0.36 | 0.00 | 6.05 | 28.0/27.5 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.48 | 5.97 | 28.1/27.6 | 24.2/24.7 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.57 | 0.43 | 0.45 | 5.88 | 33.4/21.9 | 18.8/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.70 | 0.30 | 0.00 | 9.27 | 29.5/28.9 | 23.9/22.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.083 | 0.74 | 0.26 | 0.00 | 9.32 | 35.0/23.1 | 18.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Braeden Bowman: 1+ goals YES | 13 | 0.173 | 0.161 | +0.036 | +0.024 | $6.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 65 | 0.711 | 0.694 | +0.045 | +0.028 | $20.00 | FUNDED_RESEARCH | $5 | NSH:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 18 | 0.224 | 0.211 | +0.033 | +0.021 | $5.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Victor Olofsson: 1+ goals NO | 74 | 0.780 | 0.769 | +0.027 | +0.015 | $16.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (9.96 vs 6.31 bp); relationships: KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (7.90 vs 1.38 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense succeeds (4+ goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.31 vs 5.65 bp); despite a smaller raw edge (+0.033 vs +0.034/contract); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: VGK offense suppressed (<= 2 goals)
- **Victor Olofsson: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VGK offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:SUPPRESSED (p 0.4678): highest fidelity KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4795): highest fidelity KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.3098): highest fidelity KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no (same contract)
- KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.169)
- KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3104, phi -0.255)
- KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.201)
- KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4795, phi -0.2)
- override: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.46 (adj +2.02) on $50.00, P(profit) 0.6609, adj growth 17.3 bp · B EV +4.58 (adj +2.91) on $48.58, P(profit) 0.692, adj growth 25.4 bp · C EV +3.01 (adj +1.87) on $42.62, P(profit) 0.6386, adj growth 16.5 bp · R EV +0.34 (adj +0.21) on $5.00, P(profit) 0.7106, adj growth 7.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
