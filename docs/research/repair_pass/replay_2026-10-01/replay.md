# Rules replay 2026-10-01 — DIAGNOSTIC ONLY (RESEARCH_ONLY)

_DIAGNOSTIC ONLY. Replayed at each game's final production decision instant on pregame data; no hindsight substitution. Realized P/L covers settled contracts only. This is NOT evidence that the new rules are better: it verifies that the architecture behaves as intended._

| card | bets | stake | player props | largest thesis share | mean abs phi | settled | settled stake | realized P/L | ROI (settled) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| OLD (nominal optimiser card) | 30 | 253.01 | 26 | 0.111 | 0.063 | 30 | 253.01 | -11.31 | -0.04 |
| NEW optimiser card (nominal) | 30 | 254.10 | 25 | 0.111 | 0.072 | 30 | 254.10 | -13.47 | -0.05 |
| NEW FUNDED research ($) | 11 | 36.00 | 6 | 0.139 | 0.264 | 11 | 36.00 | +4.00 | +0.11 |

shadow-only (on the optimiser card, not funded): 19 · removed by the expression-fidelity rule: 1 · removed by the market-disagreement gate: 4

## 2026020009 · cutoff 2026-10-01T22:57:03Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | 0.118 | 0.106 | 0.070 | +0.02 | FRAGILE (0.205) | 2.330 | - | LOST | -2.33 |
| OLD | KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | 0.146 | 0.136 | 0.105 | +0.02 | FRAGILE (0.269) | 2.250 | - | LOST | -2.25 |
| OLD | KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | 0.192 | 0.180 | 0.145 | +0.02 | FRAGILE (0.314) | 2.810 | - | LOST | -2.81 |
| OLD | KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes | 0.131 | 0.122 | 0.095 | +0.02 | FRAGILE (0.200) | 1.920 | - | LOST | -1.92 |
| NEW | KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | 0.118 | 0.106 | 0.070 | +0.02 | FRAGILE (0.205) | 2.360 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | 0.146 | 0.136 | 0.105 | +0.02 | FRAGILE (0.269) | 2.280 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | 0.192 | 0.180 | 0.145 | +0.02 | FRAGILE (0.314) | 2.860 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes | 0.131 | 0.122 | 0.095 | +0.02 | FRAGILE (0.200) | 1.950 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |

## 2026020010 · cutoff 2026-10-01T22:57:03Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | 0.745 | 0.615 | 0.545 | +0.05 | DIRECT (0.864) | 9.140 | - | WON | +6.97 |
| OLD | KXNHLSPREAD-26OCT01TBNYR-TB3|no | 0.848 | 0.806 | 0.765 | +0.02 | STRUCTURAL (1.000) | 9.140 | - | WON | +2.54 |
| OLD | KXNHLSPREAD-26OCT01TBNYR-TB2|no | 0.748 | 0.702 | 0.655 | +0.03 | STRUCTURAL (1.000) | 3.280 | - | WON | +1.57 |
| NEW | KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | 0.745 | 0.615 | 0.545 | +0.05 | DIRECT (0.864) | 9.270 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED $0 | WON | +0.00 |
| NEW | KXNHLSPREAD-26OCT01TBNYR-TB3|no | 0.848 | 0.806 | 0.765 | +0.02 | STRUCTURAL (1.000) | 9.270 | FUNDED_RESEARCH $3 | WON | +0.83 |
| NEW | KXNHLSPREAD-26OCT01TBNYR-TB2|no | 0.748 | 0.702 | 0.655 | +0.03 | STRUCTURAL (1.000) | 3.330 | FUNDED_RESEARCH $1 | WON | +0.48 |

## 2026020011 · cutoff 2026-10-01T22:57:03Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | 0.273 | 0.256 | 0.205 | +0.03 | FRAGILE (0.392) | 4.650 | - | LOST | -4.65 |
| OLD | KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | 0.853 | 0.844 | 0.815 | +0.01 | DIRECT (0.921) | 8.980 | - | WON | +1.84 |
| OLD | KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | 0.680 | 0.632 | 0.585 | +0.02 | DIRECT (0.827) | 4.780 | - | WON | +2.97 |
| OLD | KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | 0.691 | 0.679 | 0.645 | +0.01 | DIRECT (0.834) | 4.430 | - | WON | +2.22 |
| NEW | KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | 0.273 | 0.256 | 0.205 | +0.03 | FRAGILE (0.392) | 4.450 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | 0.853 | 0.844 | 0.815 | +0.01 | DIRECT (0.921) | 8.960 | FUNDED_RESEARCH $3 | WON | +0.61 |
| NEW | KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no | 0.861 | 0.833 | 0.805 | +0.01 | STRUCTURAL (1.000) | 6.020 | FUNDED_RESEARCH $2 | WON | +0.44 |
| NEW | KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | 0.691 | 0.679 | 0.645 | +0.01 | DIRECT (0.834) | 3.750 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | WON | +0.00 |
- substitution: Broad expression KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no selected over player prop KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

## 2026020012 · cutoff 2026-10-01T23:47:02Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes | 0.274 | 0.262 | 0.225 | +0.02 | FRAGILE (0.401) | 4.300 | - | LOST | -4.30 |
| OLD | KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no | 0.935 | 0.927 | 0.905 | +0.01 | DIRECT (0.971) | 13.840 | - | WON | +1.27 |
| OLD | KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes | 0.212 | 0.203 | 0.175 | +0.01 | FRAGILE (0.343) | 2.580 | - | LOST | -2.58 |
| OLD | KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes | 0.299 | 0.288 | 0.255 | +0.01 | FRAGILE (0.438) | 3.290 | - | LOST | -3.29 |
| NEW | KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes | 0.274 | 0.262 | 0.225 | +0.02 | FRAGILE (0.401) | 4.400 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no | 0.935 | 0.927 | 0.905 | +0.01 | DIRECT (0.971) | 14.150 | FUNDED_RESEARCH $4 | WON | +0.37 |
| NEW | KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes | 0.212 | 0.203 | 0.175 | +0.01 | FRAGILE (0.343) | 2.640 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes | 0.299 | 0.288 | 0.255 | +0.01 | FRAGILE (0.438) | 3.370 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |

## 2026020013 · cutoff 2026-10-02T01:27:03Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes | 0.167 | 0.154 | 0.115 | +0.03 | FRAGILE (0.298) | 7.010 | - | LOST | -7.01 |
| OLD | KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes | 0.265 | 0.251 | 0.210 | +0.02 | FRAGILE (0.349) | 6.560 | - | LOST | -6.56 |
| OLD | KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no | 0.774 | 0.694 | 0.650 | +0.02 | DIRECT (0.897) | 18.550 | - | LOST | -18.55 |
| OLD | KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes | 0.278 | 0.267 | 0.235 | +0.01 | FRAGILE (0.363) | 5.440 | - | WON | +16.08 |
| NEW | KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes | 0.167 | 0.154 | 0.115 | +0.03 | FRAGILE (0.298) | 7.010 | FUNDED_RESEARCH $2 | LOST | -2.00 |
| NEW | KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes | 0.265 | 0.251 | 0.210 | +0.02 | FRAGILE (0.349) | 6.560 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no | 0.774 | 0.694 | 0.650 | +0.02 | DIRECT (0.897) | 18.550 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes | 0.278 | 0.267 | 0.235 | +0.01 | FRAGILE (0.363) | 5.440 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | WON | +0.00 |

## 2026020014 · cutoff 2026-10-02T00:37:04Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no | 0.892 | 0.875 | 0.825 | +0.04 | DIRECT (0.952) | 15.330 | - | WON | +2.92 |
| OLD | KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes | 0.136 | 0.126 | 0.095 | +0.02 | FRAGILE (0.228) | 3.900 | - | WON | +32.79 |
| OLD | KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes | 0.131 | 0.122 | 0.095 | +0.02 | FRAGILE (0.212) | 3.170 | - | LOST | -3.17 |
| OLD | KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no | 0.895 | 0.885 | 0.855 | +0.02 | DIRECT (0.947) | 15.330 | - | WON | +2.32 |
| NEW | KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no | 0.892 | 0.875 | 0.825 | +0.04 | DIRECT (0.952) | 15.230 | FUNDED_RESEARCH $4 | WON | +0.76 |
| NEW | KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes | 0.136 | 0.126 | 0.095 | +0.02 | FRAGILE (0.228) | 3.880 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | WON | +0.00 |
| NEW | KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes | 0.131 | 0.122 | 0.095 | +0.02 | FRAGILE (0.212) | 3.140 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no | 0.895 | 0.885 | 0.855 | +0.02 | DIRECT (0.947) | 15.230 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | WON | +0.00 |

## 2026020015 · cutoff 2026-10-02T01:27:03Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no | 0.476 | 0.365 | 0.305 | +0.04 | DIRECT (0.705) | 8.550 | - | LOST | -8.55 |
| OLD | KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes | 0.215 | 0.200 | 0.155 | +0.03 | FRAGILE (0.338) | 8.070 | - | LOST | -8.07 |
| OLD | KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no | 0.831 | 0.717 | 0.655 | +0.03 | DIRECT (0.973) | 19.640 | - | LOST | -19.64 |
| OLD | KXNHLSPREAD-26OCT01EDMVAN-EDM3|no | 0.773 | 0.724 | 0.675 | +0.03 | STRUCTURAL (1.000) | 13.740 | - | WON | +6.02 |
| NEW | KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no | 0.476 | 0.365 | 0.305 | +0.04 | DIRECT (0.705) | 8.550 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes | 0.215 | 0.200 | 0.155 | +0.03 | FRAGILE (0.338) | 8.070 | FUNDED_RESEARCH $3 | LOST | -3.00 |
| NEW | KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no | 0.831 | 0.717 | 0.655 | +0.03 | DIRECT (0.973) | 19.640 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED $0 | LOST | +0.00 |
| NEW | KXNHLSPREAD-26OCT01EDMVAN-EDM3|no | 0.773 | 0.724 | 0.675 | +0.03 | STRUCTURAL (1.000) | 13.740 | FUNDED_RESEARCH $4 | WON | +1.75 |

## 2026020016 · cutoff 2026-10-02T01:27:03Z

reproduction of the production card by the old code: same bets True, max |p_model diff| 0.0000

| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes | 0.215 | 0.198 | 0.145 | +0.04 | FRAGILE (0.322) | 10.140 | - | LOST | -10.14 |
| OLD | KXNHLSPREAD-26OCT01FLASJ-FLA3|no | 0.852 | 0.803 | 0.755 | +0.03 | STRUCTURAL (1.000) | 19.930 | - | WON | +5.86 |
| OLD | KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no | 0.737 | 0.719 | 0.665 | +0.03 | DIRECT (0.858) | 19.930 | - | WON | +9.14 |
| NEW | KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes | 0.215 | 0.198 | 0.145 | +0.04 | FRAGILE (0.322) | 10.140 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLSPREAD-26OCT01FLASJ-FLA3|no | 0.852 | 0.803 | 0.755 | +0.03 | STRUCTURAL (1.000) | 19.930 | FUNDED_RESEARCH $5 | WON | +1.47 |
| NEW | KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no | 0.737 | 0.719 | 0.665 | +0.03 | DIRECT (0.858) | 19.930 | FUNDED_RESEARCH $5 | WON | +2.29 |
