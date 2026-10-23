# Kalshi NHL discovery summary

- discovered_at: `2026-10-23T15:53:35Z`  ontology: `2026.09.29.2`  requests: 158
- series enumerated: 15380; NHL series: 78; markets scanned: 2765

## Support states (coverage invariant)

| support | markets |
|---|---:|
| MODELABLE | 483 |
| BUILDABLE | 14 |
| RESEARCH | 1675 |
| UNMODELABLE | 548 |
| UNRESOLVED | 45 |

## NHL series

| series | family | support | fee | unopened | open | closed | settled | strike_types | parse |
|---|---|---|---|---:|---:|---:|---:|---|---|
| KXCANADACUP | season_champion | RESEARCH | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXCONNSMYTHE | season_awards | UNMODELABLE | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXESPYNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNBANHL | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNEXTTEAMNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 263 | 0 | 0 | structured | {'low': 263} |
| KXNHL | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHL1P | period_winner | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | structured | {'high': 42} |
| KXNHL1PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL1PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 28 | 0 | 0 | greater | {'high': 28} |
| KXNHL1PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | greater | {'high': 42} |
| KXNHL1STTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2OT | game_multi_overtime | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2P | period_winner | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | structured | {'high': 42} |
| KXNHL2PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 28 | 0 | 0 | greater | {'high': 28} |
| KXNHL2PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | greater | {'high': 42} |
| KXNHL30COMEBACK | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3P | period_winner | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | structured | {'high': 42} |
| KXNHL3PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 28 | 0 | 0 | greater | {'high': 28} |
| KXNHL3PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | greater | {'high': 42} |
| KXNHL4NATIONS | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLADAMS | season_awards | UNMODELABLE | quadratic/1 | 0 | 32 | 0 | 0 | custom | {'low': 32} |
| KXNHLANYGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLAST | player_assists | RESEARCH | quadratic/1 | 0 | 66 | 0 | 0 | greater | {'high': 66} |
| KXNHLATLANTIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLCALDER | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured,custom | {'low': 40} |
| KXNHLCENTRAL | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLDRAFTPICK | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLDRAFTTOP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLEAST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLEXPANSION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXNHLF10G | game_early_goal | RESEARCH | quadratic/1 | 0 | 14 | 0 | 0 | greater_or_equal | {'high': 14} |
| KXNHLFINALSEXACT | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLFIRSTGOAL | first_goal | RESEARCH | quadratic/1 | 0 | 74 | 0 | 0 | structured | {'high': 74} |
| KXNHLGAME | game_winner | MODELABLE | quadratic_with_maker_fees/1 | 0 | 96 | 0 | 0 | structured | {'high': 96} |
| KXNHLGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 125 | 0 | 0 | greater | {'high': 125} |
| KXNHLHART | season_awards | UNMODELABLE | quadratic/1 | 0 | 29 | 0 | 0 | structured | {'low': 29} |
| KXNHLLINDSAY | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 28 | 0 | 0 | structured | {'low': 28} |
| KXNHLMENTION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLMETROPOLITAN | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLMVP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTGM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 33 | 0 | 0 | structured | {'low': 33} |
| KXNHLNORRIS | season_awards | UNMODELABLE | quadratic/1 | 0 | 30 | 0 | 0 | structured | {'low': 30} |
| KXNHLOT | game_overtime | BUILDABLE | quadratic/1 | 0 | 14 | 0 | 0 | greater | {'high': 14} |
| KXNHLOVERTIME | game_overtime | BUILDABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPACIFIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLPLAYOFF | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPLAYOFFGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPRES | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPRICE | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPSEASONGOALS | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'low': 17} |
| KXNHLPTS | player_points | RESEARCH | quadratic/1 | 0 | 82 | 0 | 0 | greater | {'high': 82} |
| KXNHLRECORDWORST | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLRETIRE | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLRICHARD | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLROSS | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLSAVE | goalie_saves | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSAVES | goalie_saves | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSEASONGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 87 | 0 | 0 | greater,structured | {'low': 87} |
| KXNHLSEASONPPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 90 | 0 | 0 | greater | {'low': 90} |
| KXNHLSEASONPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 320 | 0 | 0 | greater_or_equal | {'low': 320} |
| KXNHLSERIES | playoff_series | RESEARCH | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESGAMES | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESOT | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSCORE | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSPREAD | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOAL | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOALS | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSPREAD | game_spread | MODELABLE | quadratic/1 | 0 | 76 | 0 | 0 | greater | {'high': 76} |
| KXNHLTEAMTOTAL | team_total | MODELABLE | quadratic/1 | 0 | 140 | 0 | 0 | greater | {'high': 140} |
| KXNHLTOTAL | game_total | MODELABLE | quadratic/1 | 0 | 171 | 0 | 0 | greater | {'high': 171} |
| KXNHLVEZINA | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLWEST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLWINS | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLWSTREAK | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXTEAMSINSC | season_champion | RESEARCH | quadratic/1 | 0 | 256 | 0 | 0 | custom | {'low': 256} |

## Title templates per series

### KXCANADACUP — Canada winning Stanley Cup
- (1) Will a Canadian team win the NAME® by the end of the # season?
- samples: KXCANADACUP-30
- sample fields: `{"ticker": "KXCANADACUP-30", "event_ticker": "KXCANADACUP-30", "market_type": "binary", "title": "Will a Canadian team win the Stanley Cup\u00ae by the end of the 2030 season?", "subtitle": "Before 2031", "yes_sub_title": "Before 2031", "no_sub_title": "Before 2031", "status": "active", "open_time": "2025-06-13T14:00:00Z", "close_time": "2030-06-30T03:59:00Z", "expected_expiration_time": "2030-06-30T14:00:00Z", "result": "", "rules_primary": "If a Canadian hockey team wins the Stanley Cup\u00ae after Issuance and before Jun 30, 2030, then the market resolves to Yes."}`

### KXCONNSMYTHE — Conn Smythe trophy

### KXESPYNHL — BEST NHL PLAYER‬

### KXNBANHL — NBA + NHL Champion Combo

### KXNEXTTEAMNHL — Next Team NHL
- (230) What will be NAME's next team?
- (33) What will be Connor McDavid's next team?
- samples: KXNEXTTEAMNHL-26PLAINE92-WSH, KXNEXTTEAMNHL-26PLAINE92-WPG, KXNEXTTEAMNHL-26PLAINE92-VGK, KXNEXTTEAMNHL-26PLAINE92-VAN, KXNEXTTEAMNHL-26PLAINE92-UTA, KXNEXTTEAMNHL-26PLAINE92-TOR
- sample fields: `{"ticker": "KXNEXTTEAMNHL-26PLAINE92-WSH", "event_ticker": "KXNEXTTEAMNHL-26PLAINE92", "market_type": "binary", "title": "What will be Patrik Laine's next team?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-11T19:00:00Z", "close_time": "2026-11-01T04:59:00Z", "expected_expiration_time": "2026-11-01T15:00:00Z", "result": "", "rules_primary": "If Patrik Laine's next team is Washington Capitals before Nov 1, 2026, then `

### KXNHL — Stanley Cup
- (30) NAME win the #-# NAME® Finals?
- (1) NAME. NAME win the #-# NAME® Finals?
- (1) Will Montréal Canadiens win the #-# NAME® Finals?
- samples: KXNHL-27-WSH, KXNHL-27-WPG, KXNHL-27-VGK, KXNHL-27-VAN, KXNHL-27-UTA, KXNHL-27-TOR
- sample fields: `{"ticker": "KXNHL-27-WSH", "event_ticker": "KXNHL-27", "market_type": "binary", "title": "Will Washington Capitals win the 2026-27 Stanley Cup\u00ae Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-06-15T03:40:00Z", "close_time": "2029-06-30T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals wins the 2026-27 Stanley Cup\u00ae Finals, then the marke`

### KXNHL1P — NHL 1st Period Winner
- (14) #st period tie
- (5) NAME wins the #st period
- (1) Seattle wins the #st period
- (1) Minnesota wins the #st period
- (1) Detroit wins the #st period
- (1) Calgary wins the #st period
- (1) Utah wins the #st period
- (1) Ottawa wins the #st period
- samples: KXNHL1P-26OCT24MINSEA-TIE, KXNHL1P-26OCT24MINSEA-SEA, KXNHL1P-26OCT24MINSEA-MIN, KXNHL1P-26OCT24DETCGY-TIE, KXNHL1P-26OCT24DETCGY-DET, KXNHL1P-26OCT24DETCGY-CGY
- sample fields: `{"ticker": "KXNHL1P-26OCT24MINSEA-TIE", "event_ticker": "KXNHL1P-26OCT24MINSEA", "market_type": "binary", "title": "1st period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-10-23T04:06:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If neither team wins the 1st period of the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026, then the market resolves t`

### KXNHL1PBTTS — NHL Both Teams to Score in 1st Period

### KXNHL1PSPREAD — 1st Period Spread
- (5) NAME wins #st Period by over # goals
- (1) Seattle wins #st Period by over # goals
- (1) Minnesota wins #st Period by over # goals
- (1) Detroit wins #st Period by over # goals
- (1) Calgary wins #st Period by over # goals
- (1) Utah wins #st Period by over # goals
- (1) Ottawa wins #st Period by over # goals
- (1) NAME R wins #st Period by over # goals
- samples: KXNHL1PSPREAD-26OCT24MINSEA-SEA2, KXNHL1PSPREAD-26OCT24MINSEA-MIN2, KXNHL1PSPREAD-26OCT24DETCGY-DET2, KXNHL1PSPREAD-26OCT24DETCGY-CGY2, KXNHL1PSPREAD-26OCT24TBUTA-UTA2, KXNHL1PSPREAD-26OCT24TBUTA-TB2
- sample fields: `{"ticker": "KXNHL1PSPREAD-26OCT24MINSEA-SEA2", "event_ticker": "KXNHL1PSPREAD-26OCT24MINSEA", "market_type": "binary", "title": "Seattle wins 1st Period by over 1.5 goals", "yes_sub_title": "Seattle wins by over 1.5 goals", "no_sub_title": "Seattle wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-10-23T04:06:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If Seattle wins by more th`

### KXNHL1PTOTAL — NHL 1st Period Total
- (42) #st Period: Over # goals scored
- samples: KXNHL1PTOTAL-26OCT24MINSEA-3, KXNHL1PTOTAL-26OCT24MINSEA-2, KXNHL1PTOTAL-26OCT24MINSEA-1, KXNHL1PTOTAL-26OCT24DETCGY-3, KXNHL1PTOTAL-26OCT24DETCGY-2, KXNHL1PTOTAL-26OCT24DETCGY-1
- sample fields: `{"ticker": "KXNHL1PTOTAL-26OCT24MINSEA-3", "event_ticker": "KXNHL1PTOTAL-26OCT24MINSEA", "market_type": "binary", "title": "1st Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-10-23T04:06:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 1st Period of the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026,`

### KXNHL1STTEAM — All NHL First Team

### KXNHL2OT — NHL Double Overtime

### KXNHL2P — NHL 2nd Period Winner
- (14) #nd period tie
- (5) NAME wins the #nd period
- (1) Seattle wins the #nd period
- (1) Minnesota wins the #nd period
- (1) Detroit wins the #nd period
- (1) Calgary wins the #nd period
- (1) Utah wins the #nd period
- (1) Ottawa wins the #nd period
- samples: KXNHL2P-26OCT24MINSEA-TIE, KXNHL2P-26OCT24MINSEA-SEA, KXNHL2P-26OCT24MINSEA-MIN, KXNHL2P-26OCT24DETCGY-TIE, KXNHL2P-26OCT24DETCGY-DET, KXNHL2P-26OCT24DETCGY-CGY
- sample fields: `{"ticker": "KXNHL2P-26OCT24MINSEA-TIE", "event_ticker": "KXNHL2P-26OCT24MINSEA", "market_type": "binary", "title": "2nd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-10-23T04:06:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If neither team wins the 2nd period of the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026, then the market resolves t`

### KXNHL2PBTTS — NHL Both Teams to Score in 2nd Period

### KXNHL2PSPREAD — 2nd Period Spread
- (5) NAME wins #nd Period by over # goals
- (1) Seattle wins #nd Period by over # goals
- (1) Minnesota wins #nd Period by over # goals
- (1) Detroit wins #nd Period by over # goals
- (1) Calgary wins #nd Period by over # goals
- (1) Utah wins #nd Period by over # goals
- (1) Ottawa wins #nd Period by over # goals
- (1) NAME R wins #nd Period by over # goals
- samples: KXNHL2PSPREAD-26OCT24MINSEA-SEA2, KXNHL2PSPREAD-26OCT24MINSEA-MIN2, KXNHL2PSPREAD-26OCT24DETCGY-DET2, KXNHL2PSPREAD-26OCT24DETCGY-CGY2, KXNHL2PSPREAD-26OCT24TBUTA-UTA2, KXNHL2PSPREAD-26OCT24TBUTA-TB2
- sample fields: `{"ticker": "KXNHL2PSPREAD-26OCT24MINSEA-SEA2", "event_ticker": "KXNHL2PSPREAD-26OCT24MINSEA", "market_type": "binary", "title": "Seattle wins 2nd Period by over 1.5 goals", "yes_sub_title": "Seattle wins by over 1.5 goals", "no_sub_title": "Seattle wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-10-23T04:07:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If Seattle wins by more th`

### KXNHL2PTOTAL — 2nd Period Total
- (42) #nd Period: Over # goals scored
- samples: KXNHL2PTOTAL-26OCT24MINSEA-3, KXNHL2PTOTAL-26OCT24MINSEA-2, KXNHL2PTOTAL-26OCT24MINSEA-1, KXNHL2PTOTAL-26OCT24DETCGY-3, KXNHL2PTOTAL-26OCT24DETCGY-2, KXNHL2PTOTAL-26OCT24DETCGY-1
- sample fields: `{"ticker": "KXNHL2PTOTAL-26OCT24MINSEA-3", "event_ticker": "KXNHL2PTOTAL-26OCT24MINSEA", "market_type": "binary", "title": "2nd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-10-23T04:07:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 2nd Period of the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026,`

### KXNHL30COMEBACK — NHL 3-0 Series Comeback

### KXNHL3P — NHL 3rd Period Winner
- (14) #rd period tie
- (5) NAME wins the #rd period
- (1) Seattle wins the #rd period
- (1) Minnesota wins the #rd period
- (1) Detroit wins the #rd period
- (1) Calgary wins the #rd period
- (1) Utah wins the #rd period
- (1) Ottawa wins the #rd period
- samples: KXNHL3P-26OCT24MINSEA-TIE, KXNHL3P-26OCT24MINSEA-SEA, KXNHL3P-26OCT24MINSEA-MIN, KXNHL3P-26OCT24DETCGY-TIE, KXNHL3P-26OCT24DETCGY-DET, KXNHL3P-26OCT24DETCGY-CGY
- sample fields: `{"ticker": "KXNHL3P-26OCT24MINSEA-TIE", "event_ticker": "KXNHL3P-26OCT24MINSEA", "market_type": "binary", "title": "3rd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-10-23T04:07:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If neither team wins the 3rd period (excluding overtime) of the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026, then `

### KXNHL3PBTTS — NHL Both Teams to Score in 3rd Period

### KXNHL3PSPREAD — NHL 3rd Period Spread
- (5) NAME wins #rd Period by over # goals
- (1) Seattle wins #rd Period by over # goals
- (1) Minnesota wins #rd Period by over # goals
- (1) Detroit wins #rd Period by over # goals
- (1) Calgary wins #rd Period by over # goals
- (1) Utah wins #rd Period by over # goals
- (1) Ottawa wins #rd Period by over # goals
- (1) NAME R wins #rd Period by over # goals
- samples: KXNHL3PSPREAD-26OCT24MINSEA-SEA2, KXNHL3PSPREAD-26OCT24MINSEA-MIN2, KXNHL3PSPREAD-26OCT24DETCGY-DET2, KXNHL3PSPREAD-26OCT24DETCGY-CGY2, KXNHL3PSPREAD-26OCT24TBUTA-UTA2, KXNHL3PSPREAD-26OCT24TBUTA-TB2
- sample fields: `{"ticker": "KXNHL3PSPREAD-26OCT24MINSEA-SEA2", "event_ticker": "KXNHL3PSPREAD-26OCT24MINSEA", "market_type": "binary", "title": "Seattle wins 3rd Period by over 1.5 goals", "yes_sub_title": "Seattle wins by over 1.5 goals", "no_sub_title": "Seattle wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-10-23T04:07:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If Seattle wins by more th`

### KXNHL3PTOTAL — 3rd Period Total
- (42) #rd Period: Over # goals scored
- samples: KXNHL3PTOTAL-26OCT24MINSEA-3, KXNHL3PTOTAL-26OCT24MINSEA-2, KXNHL3PTOTAL-26OCT24MINSEA-1, KXNHL3PTOTAL-26OCT24DETCGY-3, KXNHL3PTOTAL-26OCT24DETCGY-2, KXNHL3PTOTAL-26OCT24DETCGY-1
- sample fields: `{"ticker": "KXNHL3PTOTAL-26OCT24MINSEA-3", "event_ticker": "KXNHL3PTOTAL-26OCT24MINSEA", "market_type": "binary", "title": "3rd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-10-23T04:08:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 3rd Period of the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026,`

### KXNHL4NATIONS — 4 nations face off

### KXNHLADAMS — NHL Jack Adams Award
- (29) NAME: NAME wins
- (1) NAME: Todd McLellan wins
- (1) NAME: Peter DeBoer wins
- (1) NAME: NAME. Louis wins
- samples: KXNHLADAMS-27-TMCL, KXNHLADAMS-27-TGRE, KXNHLADAMS-27-SKEE, KXNHLADAMS-27-SCAR, KXNHLADAMS-27-SARN, KXNHLADAMS-27-RWAR
- sample fields: `{"ticker": "KXNHLADAMS-27-TMCL", "event_ticker": "KXNHLADAMS-27", "market_type": "binary", "title": "Jack Adams Award: Todd McLellan wins", "subtitle": "::", "yes_sub_title": "Todd McLellan", "no_sub_title": "Todd McLellan", "strike_type": "custom", "custom_strike": {"Person": "Todd McLellan"}, "status": "active", "open_time": "2026-09-28T22:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Todd McLellan wins the NHL Jack Adams Award in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLANYGOAL — Pro Hockey Goalscorer

### KXNHLAST — Pro Hockey Assists
- (58) NAME: #+ assists
- (3) Nathan MacKinnon: #+ assists
- (2) NAME D'Astous: #+ assists
- (2) Juraj Slafkovský: #+ assists
- (1) T.J. Hughes: #+ assists
- samples: KXNHLAST-26OCT23TBCOL-COLTHUGHES13-1, KXNHLAST-26OCT23MTLCHI-MTLZBOLDUC76-1, KXNHLAST-26OCT23MTLCHI-MTLJANDERSON17-1, KXNHLAST-26OCT23TBCOL-COLJSCHWARTZ71-1, KXNHLAST-26OCT23TBCOL-TBCDASTOUS51-2, KXNHLAST-26OCT23TBCOL-TBCDASTOUS51-1
- sample fields: `{"ticker": "KXNHLAST-26OCT23TBCOL-COLTHUGHES13-1", "event_ticker": "KXNHLAST-26OCT23TBCOL", "market_type": "binary", "title": "T.J. Hughes: 1+ assists", "yes_sub_title": "T.J. Hughes: 1+", "no_sub_title": "T.J. Hughes: 1+", "strike_type": "greater", "floor_strike": 0.5, "custom_strike": {"hockey_player": "38073d90-932c-4818-b513-d50bf5f065a3", "hockey_team": "70ecc991-a426-4567-b6ec-53f529f29078"}, "status": "active", "open_time": "2026-10-23T15:38:00Z", "close_time": "2026-10-26T01:00:00Z", "expected_expiration_time": "2026-10-24T07:00:00Z", "result": "", "rules_primary": "If T.J. Hughes reco`

### KXNHLATLANTIC — NHL Atlantic Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLATLANTIC-27-TOR, KXNHLATLANTIC-27-TB, KXNHLATLANTIC-27-OTT, KXNHLATLANTIC-27-MTL, KXNHLATLANTIC-27-FLA, KXNHLATLANTIC-27-DET
- sample fields: `{"ticker": "KXNHLATLANTIC-27-TOR", "event_ticker": "KXNHLATLANTIC-27", "market_type": "binary", "title": "Will the Toronto Maple Leafs win the Atlantic Division?", "yes_sub_title": "Toronto Maple Leafs", "no_sub_title": "Toronto Maple Leafs", "strike_type": "structured", "custom_strike": {"hockey_team": "f61f9daa-407b-4c46-96e8-feee19cd6f51"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Toronto Maple Leafs win the 2026-27 NHL Atlantic Division, then the `

### KXNHLCALDER — NHL Calder Memorial Trophy
- (36) NAME: NAME wins
- (1) NAME: Viggo Björck wins
- (1) NAME: NAME-Nygård wins
- (1) NAME: Gavin McKenna wins
- (1) NAME: Adam Engström wins
- samples: KXNHLCALDER-27-ZBUIUM24, KXNHLCALDER-27-VEKLUND, KXNHLCALDER-27-VBJORCK, KXNHLCALDER-27-TLINDSTEIN, KXNHLCALDER-27-TIGINLA, KXNHLCALDER-27-TCONNELLY
- sample fields: `{"ticker": "KXNHLCALDER-27-ZBUIUM24", "event_ticker": "KXNHLCALDER-27", "market_type": "binary", "title": "Calder Memorial Trophy: Zeev Buium wins", "subtitle": "::", "yes_sub_title": "Zeev Buium", "no_sub_title": "Zeev Buium", "strike_type": "structured", "custom_strike": {"hockey_player": "4e4ad45c-1cda-4e0b-89c3-4e6c27740027"}, "status": "active", "open_time": "2026-09-30T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zeev Buium wins the NHL Calder Memorial Trophy in the 2026-27 NHL season, then the ma`

### KXNHLCENTRAL — NHL Central Division Winner
- (7) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLCENTRAL-27-WPG, KXNHLCENTRAL-27-UTA, KXNHLCENTRAL-27-STL, KXNHLCENTRAL-27-NSH, KXNHLCENTRAL-27-MIN, KXNHLCENTRAL-27-DAL
- sample fields: `{"ticker": "KXNHLCENTRAL-27-WPG", "event_ticker": "KXNHLCENTRAL-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Central Division?", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Central Division, then the market resolves to Yes."}`

### KXNHLDRAFTPICK — Pro Hockey Draft Pick

### KXNHLDRAFTTOP — Pro Hockey Top Pick

### KXNHLEAST — Eastern Conference Championship
- (16) Will the NAME win the NAME?
- samples: KXNHLEAST-27-WSH, KXNHLEAST-27-TOR, KXNHLEAST-27-TB, KXNHLEAST-27-PIT, KXNHLEAST-27-PHI, KXNHLEAST-27-OTT
- sample fields: `{"ticker": "KXNHLEAST-27-WSH", "event_ticker": "KXNHLEAST-27", "market_type": "binary", "title": "Will the Washington Capitals win the Eastern Conference Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Eastern Conference Finals, t`

### KXNHLEXPANSION — NHL Expansion
- (1) NAME receive an NHL expansion team before #?
- samples: KXNHLEXPANSION-27JAN01HOU-Y
- sample fields: `{"ticker": "KXNHLEXPANSION-27JAN01HOU-Y", "event_ticker": "KXNHLEXPANSION-27JAN01HOU", "market_type": "binary", "title": "Will Houston receive an NHL expansion team before 2027?", "yes_sub_title": "Houston to get an expansion team before 2027", "no_sub_title": "Houston to get an expansion team before 2027", "status": "active", "open_time": "2026-09-01T01:00:00Z", "close_time": "2027-01-01T04:59:00Z", "expected_expiration_time": "2027-01-01T15:00:00Z", "result": "", "rules_primary": "If the NHL officially announces the award of an expansion team franchise to Houston before Jan 1, 2027, then the`

### KXNHLF10G — NHL Goal in First 10 Minutes
- (14) Either team to score in the first # minutes
- samples: KXNHLF10G-26OCT24MINSEA-Y, KXNHLF10G-26OCT24DETCGY-Y, KXNHLF10G-26OCT24TBUTA-Y, KXNHLF10G-26OCT24NYROTT-Y, KXNHLF10G-26OCT24CARSTL-Y, KXNHLF10G-26OCT24VGKCBJ-Y
- sample fields: `{"ticker": "KXNHLF10G-26OCT24MINSEA-Y", "event_ticker": "KXNHLF10G-26OCT24MINSEA", "market_type": "binary", "title": "Either team to score in the first 10 minutes", "yes_sub_title": "Goal in first 10 min", "no_sub_title": "Goal in first 10 min", "strike_type": "greater_or_equal", "floor_strike": 1, "status": "active", "open_time": "2026-10-23T04:06:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If at least 1 goal is scored by either Minnesota or Seattle during the first 10 minutes of the first period (from 0:00 el`

### KXNHLFINALSEXACT — NHL Championship Series Score

### KXNHLFIRSTGOAL — NHL First Goal
- (67) NAME: NAME
- (1) Ryan McDonagh: NAME
- (1) J.J. Moser: NAME
- (1) NAME D'Astous: NAME
- (1) T.J. Hughes: NAME
- (1) Nathan MacKinnon: NAME
- (1) Logan O'Connor: NAME
- (1) Juraj Slafkovský: NAME
- samples: KXNHLFIRSTGOAL-26OCT23TBCOL-TBZGIRGENSONS28, KXNHLFIRSTGOAL-26OCT23TBCOL-TBVHEDMAN77, KXNHLFIRSTGOAL-26OCT23TBCOL-TBRMCDONAGH27, KXNHLFIRSTGOAL-26OCT23TBCOL-TBPHOLMBERG29, KXNHLFIRSTGOAL-26OCT23TBCOL-TBNKUCHEROV86, KXNHLFIRSTGOAL-26OCT23TBCOL-TBJVIEL25
- sample fields: `{"ticker": "KXNHLFIRSTGOAL-26OCT23TBCOL-TBZGIRGENSONS28", "event_ticker": "KXNHLFIRSTGOAL-26OCT23TBCOL", "market_type": "binary", "title": "Zemgus Girgensons: First Goalscorer", "yes_sub_title": "Zemgus Girgensons", "no_sub_title": "Zemgus Girgensons", "strike_type": "structured", "custom_strike": {"hockey_player": "276cce54-f637-4129-833c-fb7cccb66495", "hockey_team": "b08e569c-3249-4fcf-bea2-a57ab5e822eb"}, "status": "active", "open_time": "2026-10-23T13:05:00Z", "close_time": "2026-10-26T01:00:00Z", "expected_expiration_time": "2026-10-24T04:00:00Z", "result": "", "rules_primary": "If Zemgu`

### KXNHLGAME — NHL Game
- (13) NAME wins
- (4) Nashville wins
- (4) Montreal wins
- (4) Minnesota wins
- (4) Chicago wins
- (3) Vancouver wins
- (3) Buffalo wins
- (3) Anaheim wins
- samples: KXNHLGAME-26OCT29VANSJ-VAN, KXNHLGAME-26OCT29VANSJ-SJ, KXNHLGAME-26OCT29BUFANA-BUF, KXNHLGAME-26OCT29BUFANA-ANA, KXNHLGAME-26OCT29OTTLA-OTT, KXNHLGAME-26OCT29OTTLA-LA
- sample fields: `{"ticker": "KXNHLGAME-26OCT29VANSJ-VAN", "event_ticker": "KXNHLGAME-26OCT29VANSJ", "market_type": "binary", "title": "Vancouver wins", "yes_sub_title": "Vancouver", "no_sub_title": "Vancouver", "strike_type": "structured", "custom_strike": {"hockey_team": "2d6db4a4-99f2-4547-85f3-9913404577f9"}, "status": "active", "open_time": "2026-10-23T04:09:00Z", "close_time": "2026-11-01T02:00:00Z", "expected_expiration_time": "2026-10-30T05:00:00Z", "result": "", "rules_primary": "If Vancouver wins the Vancouver vs San Jose NHL game originally scheduled for Oct 29, 2026, then the market resolves to Yes.`

### KXNHLGOAL — NHL Goalscorer
- (113) NAME: #+ goals
- (3) Nathan MacKinnon: #+ goals
- (3) Juraj Slafkovský: #+ goals
- (2) T.J. Hughes: #+ goals
- (1) Ryan McDonagh: #+ goals
- (1) J.J. Moser: #+ goals
- (1) NAME D'Astous: #+ goals
- (1) Logan O'Connor: #+ goals
- samples: KXNHLGOAL-26OCT23TBCOL-TBZGIRGENSONS28-2, KXNHLGOAL-26OCT23TBCOL-TBZGIRGENSONS28-1, KXNHLGOAL-26OCT23TBCOL-TBVHEDMAN77-1, KXNHLGOAL-26OCT23TBCOL-TBRMCDONAGH27-1, KXNHLGOAL-26OCT23TBCOL-TBPHOLMBERG29-2, KXNHLGOAL-26OCT23TBCOL-TBPHOLMBERG29-1
- sample fields: `{"ticker": "KXNHLGOAL-26OCT23TBCOL-TBZGIRGENSONS28-2", "event_ticker": "KXNHLGOAL-26OCT23TBCOL", "market_type": "binary", "title": "Zemgus Girgensons: 2+ goals", "yes_sub_title": "Zemgus Girgensons: 2+", "no_sub_title": "Zemgus Girgensons: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "276cce54-f637-4129-833c-fb7cccb66495", "hockey_team": "b08e569c-3249-4fcf-bea2-a57ab5e822eb"}, "status": "active", "open_time": "2026-10-23T13:05:00Z", "close_time": "2026-10-26T01:00:00Z", "expected_expiration_time": "2026-10-24T04:00:00Z", "result": "", "rules_primary":`

### KXNHLHART — NHL Hart Memorial Trophy
- (28) Who will win NAME?
- (1) NAME: NAME wins
- samples: KXNHLHART-27-ALAFRENIERE13, KXNHLHART-27-WNYLANDER88, KXNHLHART-27-SCROSBY87, KXNHLHART-27-QHUGHES43, KXNHLHART-27-PDOROFEYEV16, KXNHLHART-27-NSUZUKI14
- sample fields: `{"ticker": "KXNHLHART-27-ALAFRENIERE13", "event_ticker": "KXNHLHART-27", "market_type": "binary", "title": "Hart Memorial Trophy: Alexis Lafreniere wins", "yes_sub_title": "Alexis Lafreniere", "no_sub_title": "Alexis Lafreniere", "strike_type": "structured", "custom_strike": {"hockey_player": "10ed52fe-025d-4478-ac36-6a104f1fae78"}, "status": "active", "open_time": "2026-10-14T23:00:00Z", "close_time": "2027-06-30T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Alexis Lafreniere wins the NHL Hart Memorial Trophy in the 2026-27 NHL season, then`

### KXNHLLINDSAY — NHL Ted Lindsay Winner
- (26) NAME: NAME wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLLINDSAY-27-WNYLANDER88, KXNHLLINDSAY-27-SCROSBY87, KXNHLLINDSAY-27-QHUGHES43, KXNHLLINDSAY-27-PDOROFEYEV16, KXNHLLINDSAY-27-NSUZUKI14, KXNHLLINDSAY-27-NMACKINNON29
- sample fields: `{"ticker": "KXNHLLINDSAY-27-WNYLANDER88", "event_ticker": "KXNHLLINDSAY-27", "market_type": "binary", "title": "Ted Lindsay Award: William Nylander wins", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-10-08T02:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Ted Lindsay Award in the 2026-27 NHL `

### KXNHLMENTION — NHL Announcer Mentions

### KXNHLMETROPOLITAN — NHL Metropolitan Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLMETROPOLITAN-27-WSH, KXNHLMETROPOLITAN-27-PIT, KXNHLMETROPOLITAN-27-PHI, KXNHLMETROPOLITAN-27-NYR, KXNHLMETROPOLITAN-27-NYI, KXNHLMETROPOLITAN-27-NJ
- sample fields: `{"ticker": "KXNHLMETROPOLITAN-27-WSH", "event_ticker": "KXNHLMETROPOLITAN-27", "market_type": "binary", "title": "Will the Washington Capitals win the Metropolitan Division?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Metropolitan Div`

### KXNHLMVP — NHL Hart Memorial Trophy Winner

### KXNHLNEXTGM — Next NHL GM

### KXNHLNEXTTEAM — NHL Next Team
- (31) NAME' next team before Nov #, #: NAME
- (1) NAME' next team before Nov #, #: St. NAME
- (1) NAME' next team before Nov #, #: Retires / NAME
- samples: KXNHLNEXTTEAM-26QHUGHES43-WSH, KXNHLNEXTTEAM-26QHUGHES43-WPG, KXNHLNEXTTEAM-26QHUGHES43-VGK, KXNHLNEXTTEAM-26QHUGHES43-VAN, KXNHLNEXTTEAM-26QHUGHES43-UTA, KXNHLNEXTTEAM-26QHUGHES43-TOR
- sample fields: `{"ticker": "KXNHLNEXTTEAM-26QHUGHES43-WSH", "event_ticker": "KXNHLNEXTTEAM-26QHUGHES43", "market_type": "binary", "title": "Quinn Hughes' next team before Nov 1, 2026: Washington Capitals", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:00:00Z", "close_time": "2026-11-01T04:59:00Z", "expected_expiration_time": "2026-11-01T15:00:00Z", "result": "", "rules_primary": "If Quinn Hughes' \nnext team is the Washington Ca`

### KXNHLNORRIS — NHL James Norris Memorial Trophy
- (28) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Charlie McAvoy wins
- samples: KXNHLNORRIS-27-ZWERENSKI8, KXNHLNORRIS-27-VHEDMAN77, KXNHLNORRIS-27-THARLEY55, KXNHLNORRIS-27-STHEODORE27, KXNHLNORRIS-27-RSANDIN38, KXNHLNORRIS-27-RJOSI59
- sample fields: `{"ticker": "KXNHLNORRIS-27-ZWERENSKI8", "event_ticker": "KXNHLNORRIS-27", "market_type": "binary", "title": "James Norris Memorial Trophy: Zach Werenski wins", "subtitle": "::", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "structured", "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zach Werenski wins the NHL James Norris Memorial Trophy in the 2026-`

### KXNHLOT — NHL Overtime
- (14) Game goes to overtime
- samples: KXNHLOT-26OCT24MINSEA-1, KXNHLOT-26OCT24DETCGY-1, KXNHLOT-26OCT24TBUTA-1, KXNHLOT-26OCT24NYROTT-1, KXNHLOT-26OCT24CARSTL-1, KXNHLOT-26OCT24VGKCBJ-1
- sample fields: `{"ticker": "KXNHLOT-26OCT24MINSEA-1", "event_ticker": "KXNHLOT-26OCT24MINSEA", "market_type": "binary", "title": "Game goes to overtime", "yes_sub_title": "Game goes to overtime", "no_sub_title": "Game goes to overtime", "strike_type": "greater", "floor_strike": 0.5, "status": "active", "open_time": "2026-10-23T04:08:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If at least 1 overtime period is played in the Minnesota vs Seattle NHL game originally scheduled for Oct 24, 2026, then the market resolves to Yes."}`

### KXNHLOVERTIME — NHL Overtime

### KXNHLPACIFIC — NHL Pacific Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLPACIFIC-27-VGK, KXNHLPACIFIC-27-VAN, KXNHLPACIFIC-27-SJ, KXNHLPACIFIC-27-SEA, KXNHLPACIFIC-27-LA, KXNHLPACIFIC-27-EDM
- sample fields: `{"ticker": "KXNHLPACIFIC-27-VGK", "event_ticker": "KXNHLPACIFIC-27", "market_type": "binary", "title": "Will the Vegas Golden Knights win the Pacific Division?", "yes_sub_title": "Vegas Golden Knights", "no_sub_title": "Vegas Golden Knights", "strike_type": "structured", "custom_strike": {"hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Vegas Golden Knights win the 2026-27 NHL Pacific Division, then the `

### KXNHLPLAYOFF — Playoff Qualifier
- (30) Will the NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the St. NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the Montréal Canadiens qualify for the playoffs in the #-# NHL season?
- samples: KXNHLPLAYOFF-27-WSH, KXNHLPLAYOFF-27-WPG, KXNHLPLAYOFF-27-VGK, KXNHLPLAYOFF-27-VAN, KXNHLPLAYOFF-27-UTA, KXNHLPLAYOFF-27-TOR
- sample fields: `{"ticker": "KXNHLPLAYOFF-27-WSH", "event_ticker": "KXNHLPLAYOFF-27", "market_type": "binary", "title": "Will the Washington Capitals qualify for the playoffs in the 2026-27 NHL season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals qualify for the playoffs `

### KXNHLPLAYOFFGOALS — NHL Playoffs Goal Leader (by Round)

### KXNHLPRES — NHL President's Trophy Winner
- (30) Will the NAME win the Presidents' Trophy?
- (1) Will the St. NAME win the Presidents' Trophy?
- (1) Will the Montréal Canadiens win the Presidents' Trophy?
- samples: KXNHLPRES-27-WSH, KXNHLPRES-27-WPG, KXNHLPRES-27-VGK, KXNHLPRES-27-VAN, KXNHLPRES-27-UTA, KXNHLPRES-27-TOR
- sample fields: `{"ticker": "KXNHLPRES-27-WSH", "event_ticker": "KXNHLPRES-27", "market_type": "binary", "title": "Will the Washington Capitals win the Presidents' Trophy?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-14T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Presidents' Trophy, then the market`

### KXNHLPRICE — NHL Ticket Prices

### KXNHLPSEASONGOALS — Player Goals Scored in Season
- (17) NAME: #+ goals in #-# NHL regular season?
- samples: KXNHLPSEASONGOALS-27MCELEBRINI71-60, KXNHLPSEASONGOALS-27MCELEBRINI71-55, KXNHLPSEASONGOALS-27MCELEBRINI71-50, KXNHLPSEASONGOALS-27MCELEBRINI71-45, KXNHLPSEASONGOALS-27MCELEBRINI71-40, KXNHLPSEASONGOALS-27MCELEBRINI71-35
- sample fields: `{"ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71-60", "event_ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71", "market_type": "binary", "title": "Macklin Celebrini: 60+ goals in 2026-27 NHL regular season?", "subtitle": "Macklin Celebrini", "yes_sub_title": "60+ goals", "no_sub_title": "60+ goals", "strike_type": "greater", "floor_strike": 59.5, "custom_strike": {"hockey_player": "264560c4-3624-4c01-924e-879a08799f16"}, "status": "active", "open_time": "2026-10-09T01:30:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Mac`

### KXNHLPTS — Pro Hockey Points
- (71) NAME: #+ points
- (4) Nathan MacKinnon: #+ points
- (3) Juraj Slafkovský: #+ points
- (2) T.J. Hughes: #+ points
- (2) NAME D'Astous: #+ points
- samples: KXNHLPTS-26OCT23TBCOL-COLTHUGHES13-2, KXNHLPTS-26OCT23TBCOL-COLTHUGHES13-1, KXNHLPTS-26OCT23MTLCHI-MTLZBOLDUC76-2, KXNHLPTS-26OCT23MTLCHI-MTLZBOLDUC76-1, KXNHLPTS-26OCT23MTLCHI-MTLJANDERSON17-2, KXNHLPTS-26OCT23MTLCHI-MTLJANDERSON17-1
- sample fields: `{"ticker": "KXNHLPTS-26OCT23TBCOL-COLTHUGHES13-2", "event_ticker": "KXNHLPTS-26OCT23TBCOL", "market_type": "binary", "title": "T.J. Hughes: 2+ points", "yes_sub_title": "T.J. Hughes: 2+", "no_sub_title": "T.J. Hughes: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "38073d90-932c-4818-b513-d50bf5f065a3", "hockey_team": "70ecc991-a426-4567-b6ec-53f529f29078"}, "status": "active", "open_time": "2026-10-23T15:38:00Z", "close_time": "2026-10-26T01:00:00Z", "expected_expiration_time": "2026-10-24T07:00:00Z", "result": "", "rules_primary": "If T.J. Hughes recor`

### KXNHLRECORDWORST — Worst NHL Record
- (30) Will the NAME have the worst regular season record in the #-# season?
- (1) Will the St. NAME have the worst regular season record in the #-# season?
- (1) Will the Montréal Canadiens have the worst regular season record in the #-# season?
- samples: KXNHLRECORDWORST-27-WSH, KXNHLRECORDWORST-27-WPG, KXNHLRECORDWORST-27-VGK, KXNHLRECORDWORST-27-VAN, KXNHLRECORDWORST-27-UTA, KXNHLRECORDWORST-27-TOR
- sample fields: `{"ticker": "KXNHLRECORDWORST-27-WSH", "event_ticker": "KXNHLRECORDWORST-27", "market_type": "binary", "title": "Will the Washington Capitals have the worst regular season record in the 2026-27 season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-29T16:00:00Z", "close_time": "2027-05-31T14:00:00Z", "expected_expiration_time": "2027-05-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals have the `

### KXNHLRETIRE — NHL Retire

### KXNHLRICHARD — NHL Maurice "Rocket" Richard Trophy
- (37) Maurice "Rocket" NAME: NAME wins
- (1) Maurice "Rocket" NAME: Nathan MacKinnon wins
- (1) Maurice "Rocket" NAME: Connor McDavid wins
- (1) Maurice "Rocket" NAME: Alex DeBrincat wins
- samples: KXNHLRICHARD-27-ZHYMAN18, KXNHLRICHARD-27-WNYLANDER88, KXNHLRICHARD-27-WJOHNSTON53, KXNHLRICHARD-27-TTHOMPSON72, KXNHLRICHARD-27-SSTAMKOS91, KXNHLRICHARD-27-SREINHART13
- sample fields: `{"ticker": "KXNHLRICHARD-27-ZHYMAN18", "event_ticker": "KXNHLRICHARD-27", "market_type": "binary", "title": "Maurice \"Rocket\" Richard Trophy: Zach Hyman wins", "subtitle": "::", "yes_sub_title": "Zach Hyman", "no_sub_title": "Zach Hyman", "strike_type": "structured", "custom_strike": {"hockey_player": "2c3d67df-721b-4ea4-8aee-dea4a9715c82"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zach Hyman wins the NHL Maurice \"Rocket\" Richard Award in the 2026-27 `

### KXNHLROSS — NHL Art Ross Trophy
- (38) NAME: NAME wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLROSS-27-WNYLANDER88, KXNHLROSS-27-WJOHNSTON53, KXNHLROSS-27-TTHOMPSON72, KXNHLROSS-27-TSTUTZLE18, KXNHLROSS-27-SREINHART13, KXNHLROSS-27-SJARVIS24
- sample fields: `{"ticker": "KXNHLROSS-27-WNYLANDER88", "event_ticker": "KXNHLROSS-27", "market_type": "binary", "title": "Art Ross Trophy: William Nylander wins", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Art Ross Trophy in the 2026-27 NHL season, th`

### KXNHLSAVE — Goaltender Saves

### KXNHLSAVES — Pro Hockey Saves

### KXNHLSEASONGOALS — Player to score X Goals in Season
- (81) NAME: #+ goals in #-# NHL regular season?
- (2) Nathan MacKinnon: #+ goals in #-# NHL regular season?
- (2) Connor McDavid: #+ goals in #-# NHL regular season?
- (2) Alex DeBrincat: #+ goals in #-# NHL regular season?
- samples: KXNHLSEASONGOALS-27C40-BTKACHUK8, KXNHLSEASONGOALS-27C20-WSMITH2, KXNHLSEASONGOALS-27C20-SCROSBY87, KXNHLSEASONGOALS-27C20-PKANE88, KXNHLSEASONGOALS-27C20-MSCHAEFER48, KXNHLSEASONGOALS-27C20-FNAZAR91
- sample fields: `{"ticker": "KXNHLSEASONGOALS-27C40-BTKACHUK8", "event_ticker": "KXNHLSEASONGOALS-27C40", "market_type": "binary", "title": "Brady Tkachuk: 40+ goals in 2026-27 NHL regular season?", "subtitle": "Brady Tkachuk:: FLA Panthers", "yes_sub_title": "Brady Tkachuk", "no_sub_title": "Brady Tkachuk", "strike_type": "greater", "floor_strike": 39.5, "custom_strike": {"hockey_player": "3d7e2b4d-d4a8-4fe2-904f-fbfb0773ed66"}, "status": "active", "open_time": "2026-10-14T16:35:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If B`

### KXNHLSEASONPPTS — Season Player Points
- (84) NAME: #+ points in #-# NHL regular season?
- (3) Nathan MacKinnon: #+ points in #-# NHL regular season?
- (3) Connor McDavid: #+ points in #-# NHL regular season?
- samples: KXNHLSEASONPPTS-27C110-ZWERENSKI8, KXNHLSEASONPPTS-27C110-WNYLANDER88, KXNHLSEASONPPTS-27C110-WJOHNSTON53, KXNHLSEASONPPTS-27C110-TSTUTZLE18, KXNHLSEASONPPTS-27C110-SCROSBY87, KXNHLSEASONPPTS-27C110-NSUZUKI14
- sample fields: `{"ticker": "KXNHLSEASONPPTS-27C110-ZWERENSKI8", "event_ticker": "KXNHLSEASONPPTS-27C110", "market_type": "binary", "title": "Zach Werenski: 110+ points in 2026-27 NHL regular season?", "subtitle": "Zach Werenski:: Columbus Blue Jackets", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "greater", "floor_strike": 109.5, "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_pr`

### KXNHLSEASONPTS — NHL Season Point Totals
- (10) Will the WSH Capitals NHL team earn at least # points in the #-# regular season?
- (10) Will the WPG Jets NHL team earn at least # points in the #-# regular season?
- (10) Will the VGK NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the VAN Canucks NHL team earn at least # points in the #-# regular season?
- (10) Will the UTA Mammoth NHL team earn at least # points in the #-# regular season?
- (10) Will the TOR NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the TB Lightning NHL team earn at least # points in the #-# regular season?
- (10) Will the STL Blues NHL team earn at least # points in the #-# regular season?
- samples: KXNHLSEASONPTS-27WSH-95, KXNHLSEASONPTS-27WSH-90, KXNHLSEASONPTS-27WSH-85, KXNHLSEASONPTS-27WSH-80, KXNHLSEASONPTS-27WSH-75, KXNHLSEASONPTS-27WSH-70
- sample fields: `{"ticker": "KXNHLSEASONPTS-27WSH-95", "event_ticker": "KXNHLSEASONPTS-27WSH", "market_type": "binary", "title": "Will the WSH Capitals NHL team earn at least 95 points in the 2026-27 regular season?", "yes_sub_title": "95+ points", "no_sub_title": "95+ points", "strike_type": "greater_or_equal", "floor_strike": 95, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:47:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-18T14:00:00Z", "result": "", "rules_primary": "If the WSH Capitals earn at le`

### KXNHLSERIES — NHL Series Winner

### KXNHLSERIESGAMES — NHL Series Total Games

### KXNHLSERIESOT — NHL Series Overtime

### KXNHLSERIESSCORE — NHL Series Exact Score

### KXNHLSERIESSPREAD — NHL Series Game Spread

### KXNHLSERIESTOTALGOAL — NHL Series Total Goals

### KXNHLSERIESTOTALGOALS — NHL Series Total Goals

### KXNHLSPREAD — NHL Spread
- (10) NAME wins by over # goals
- (4) Minnesota wins by over # goals
- (4) Nashville wins by over # goals
- (4) Colorado wins by over # goals
- (4) Montreal wins by over # goals
- (4) Chicago wins by over # goals
- (2) Vancouver wins by over # goals
- (2) Winnipeg wins by over # goals
- samples: KXNHLSPREAD-26OCT25MINVAN-VAN3, KXNHLSPREAD-26OCT25MINVAN-VAN2, KXNHLSPREAD-26OCT25MINVAN-MIN3, KXNHLSPREAD-26OCT25MINVAN-MIN2, KXNHLSPREAD-26OCT25COLNSH-NSH3, KXNHLSPREAD-26OCT25COLNSH-NSH2
- sample fields: `{"ticker": "KXNHLSPREAD-26OCT25MINVAN-VAN3", "event_ticker": "KXNHLSPREAD-26OCT25MINVAN", "market_type": "binary", "title": "Vancouver wins by over 2.5 goals", "yes_sub_title": "Vancouver wins by over 2.5 goals", "no_sub_title": "Vancouver wins by over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_team": "2d6db4a4-99f2-4547-85f3-9913404577f9"}, "status": "active", "open_time": "2026-10-23T04:08:00Z", "close_time": "2026-10-28T02:00:00Z", "expected_expiration_time": "2026-10-26T05:00:00Z", "result": "", "rules_primary": "If Vancouver wins by over 2.5 goals`

### KXNHLTEAMTOTAL — NHL Team Goals Scored During Game
- (25) NAME over # goals scored
- (5) Seattle over # goals scored
- (5) Minnesota over # goals scored
- (5) Detroit over # goals scored
- (5) Calgary over # goals scored
- (5) Utah over # goals scored
- (5) Ottawa over # goals scored
- (5) NAME R over # goals scored
- samples: KXNHLTEAMTOTAL-26OCT24MINSEA-SEA6, KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5, KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4, KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3, KXNHLTEAMTOTAL-26OCT24MINSEA-SEA2, KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6
- sample fields: `{"ticker": "KXNHLTEAMTOTAL-26OCT24MINSEA-SEA6", "event_ticker": "KXNHLTEAMTOTAL-26OCT24MINSEA", "market_type": "binary", "title": "Seattle over 5.5 goals scored", "yes_sub_title": "Seattle over 5.5", "no_sub_title": "Seattle over 5.5", "strike_type": "greater", "floor_strike": 5.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-10-23T04:06:00Z", "close_time": "2026-10-27T02:00:00Z", "expected_expiration_time": "2026-10-25T05:00:00Z", "result": "", "rules_primary": "If Seattle scores over 5.5 goals in the Minnesota vs Seattle NHL`

### KXNHLTOTAL — NHL Total Goals
- (171) NAME: Over # goals scored
- samples: KXNHLTOTAL-26OCT25MINVAN-9, KXNHLTOTAL-26OCT25MINVAN-8, KXNHLTOTAL-26OCT25MINVAN-7, KXNHLTOTAL-26OCT25MINVAN-6, KXNHLTOTAL-26OCT25MINVAN-5, KXNHLTOTAL-26OCT25MINVAN-4
- sample fields: `{"ticker": "KXNHLTOTAL-26OCT25MINVAN-9", "event_ticker": "KXNHLTOTAL-26OCT25MINVAN", "market_type": "binary", "title": "Full Game: Over 8.5 goals scored", "yes_sub_title": "Over 8.5 goals scored", "no_sub_title": "Over 8.5 goals scored", "strike_type": "greater", "floor_strike": 8.5, "status": "active", "open_time": "2026-10-23T04:08:00Z", "close_time": "2026-10-28T02:00:00Z", "expected_expiration_time": "2026-10-26T05:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 8.5 goals in the Minnesota vs Vancouver NHL game originally scheduled for Oct 25, 2026, then t`

### KXNHLVEZINA — NHL Vezina Trophy
- (40) NAME: NAME wins
- samples: KXNHLVEZINA-27-YASKAROV30, KXNHLVEZINA-27-ULUUKKONEN1, KXNHLVEZINA-27-TDEMKO35, KXNHLVEZINA-27-SSKINNER74, KXNHLVEZINA-27-SMONTEMBEAULT35, KXNHLVEZINA-27-SKNIGHT30
- sample fields: `{"ticker": "KXNHLVEZINA-27-YASKAROV30", "event_ticker": "KXNHLVEZINA-27", "market_type": "binary", "title": "Vezina Trophy: Yaroslav Askarov wins", "subtitle": "::", "yes_sub_title": "Yaroslav Askarov", "no_sub_title": "Yaroslav Askarov", "strike_type": "structured", "custom_strike": {"hockey_player": "d9975a58-bdda-4de9-9933-549069713e00"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Yaroslav Askarov wins the NHL Vezina Trophy in the 2026-27 NHL season, the`

### KXNHLWEST — Western Conference Champion
- (15) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLWEST-27-WPG, KXNHLWEST-27-VGK, KXNHLWEST-27-VAN, KXNHLWEST-27-UTA, KXNHLWEST-27-STL, KXNHLWEST-27-SJ
- sample fields: `{"ticker": "KXNHLWEST-27-WPG", "event_ticker": "KXNHLWEST-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Western Conference Finals?", "subtitle": "Winnipeg Jets", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Western Conference Fina`

### KXNHLWINS — NHL wins 

### KXNHLWSTREAK — Longest NHL win streak in regular season
- (30) Will the NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the St. NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the Montréal Canadiens have the longest winning streak in the #-# NHL regular season?
- samples: KXNHLWSTREAK-27-WSH, KXNHLWSTREAK-27-WPG, KXNHLWSTREAK-27-VGK, KXNHLWSTREAK-27-VAN, KXNHLWSTREAK-27-UTA, KXNHLWSTREAK-27-TOR
- sample fields: `{"ticker": "KXNHLWSTREAK-27-WSH", "event_ticker": "KXNHLWSTREAK-27", "market_type": "binary", "title": "Will the Washington Capitals have the longest winning streak in the 2026-27 NHL regular season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals has the longes`

### KXTEAMSINSC — Teams in Stanley Cup
- (1) Will WSH Capitals vs WPG Jets be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VGK NAME be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VAN Canucks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs UTA Mammoth be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs STL Blues be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SJ Sharks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SEA Kraken be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs NSH Predators be the matchup in the #-# NAME?
- samples: KXTEAMSINSC-27-WSHWPG, KXTEAMSINSC-27-WSHVGK, KXTEAMSINSC-27-WSHVAN, KXTEAMSINSC-27-WSHUTA, KXTEAMSINSC-27-WSHSTL, KXTEAMSINSC-27-WSHSJ
- sample fields: `{"ticker": "KXTEAMSINSC-27-WSHWPG", "event_ticker": "KXTEAMSINSC-27", "market_type": "binary", "title": "Will WSH Capitals vs WPG Jets be the matchup in the 2026-27 Stanley Cup Final?", "yes_sub_title": "WSH Capitals vs WPG Jets", "no_sub_title": "WSH Capitals vs WPG Jets", "strike_type": "custom", "custom_strike": {"Matchup": "WSH Capitals vs WPG Jets"}, "status": "active", "open_time": "2026-09-11T22:00:00Z", "close_time": "2027-06-15T14:00:00Z", "expected_expiration_time": "2027-06-15T14:00:00Z", "result": "", "rules_primary": "If WSH Capitals vs WPG Jets is confirmed to be the matchup in t`

## UNRESOLVED samples

- `KXNHLLINDSAY-27-WNYLANDER88` — Ted Lindsay Award: William Nylander wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-SCROSBY87` — Ted Lindsay Award: Sidney Crosby wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-QHUGHES43` — Ted Lindsay Award: Quinn Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-PDOROFEYEV16` — Ted Lindsay Award: Pavel Dorofeyev wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NSUZUKI14` — Ted Lindsay Award: Nick Suzuki wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NMACKINNON29` — Ted Lindsay Award: Nathan MacKinnon wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NKUCHEROV86` — Ted Lindsay Award: Nikita Kucherov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MTKACHUK19` — Ted Lindsay Award: Matthew Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MRANTANEN96` — Ted Lindsay Award: Mikko Rantanen wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MMARNER93` — Ted Lindsay Award: Mitch Marner wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MCELEBRINI71` — Ted Lindsay Award: Macklin Celebrini wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-LDRAISAITL29` — Ted Lindsay Award: Leon Draisaitl wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KKAPRIZOV97` — Ted Lindsay Award: Kirill Kaprizov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KCONNOR81` — Ted Lindsay Award: Kyle Connor wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JHUGHES86` — Ted Lindsay Award: Jack Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JEICHEL9` — Ted Lindsay Award: Jack Eichel wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-ISHESTERKIN31` — Ted Lindsay Award: Igor Shesterkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-DPASTRNAK88` — Ted Lindsay Award: David Pastrnak wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMCDAVID97` — Ted Lindsay Award: Connor McDavid wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMAKAR8` — Ted Lindsay Award: Cale Makar wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CHELLEBUYCK37` — Ted Lindsay Award: Connor Hellebuyck wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CCAUFIELD13` — Ted Lindsay Award: Cole Caufield wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CBEDARD98` — Ted Lindsay Award: Connor Bedard wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-BTKACHUK7` — Ted Lindsay Award: Brady Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AVASILEVSKIY88` — Ted Lindsay Award: Andrei Vasilevskiy wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-APANARIN72` — Ted Lindsay Award: Artemi Panarin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AOVECHKIN8` — Ted Lindsay Award: Alex Ovechkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AMATTHEWS34` — Ted Lindsay Award: Auston Matthews wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-60` — Macklin Celebrini: 60+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-55` — Macklin Celebrini: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-50` — Macklin Celebrini: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-45` — Macklin Celebrini: 45+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-40` — Macklin Celebrini: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-35` — Macklin Celebrini: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-30` — Macklin Celebrini: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-25` — Macklin Celebrini: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-20` — Macklin Celebrini: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-55` — Alex Ovechkin: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-50` — Alex Ovechkin: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-40` — Alex Ovechkin: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-35` — Alex Ovechkin: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-30` — Alex Ovechkin: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-25` — Alex Ovechkin: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-20` — Alex Ovechkin: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-15` — Alex Ovechkin: 15+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title

## Series decisions (hockey-related)

- NHL  `KXNHLSERIESSCORE` NHL Series Exact Score — ticker prefix KXNHL
- NHL  `KXNHLSPREAD` NHL Spread — ticker prefix KXNHL
- NHL  `KXNHL1PBTTS` NHL Both Teams to Score in 1st Period — ticker prefix KXNHL
- skip `KXLIIGA` Liiga Champion — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHLGAME` NHL Game — ticker prefix KXNHL
- NHL  `KXNHL2P` NHL 2nd Period Winner — ticker prefix KXNHL
- skip `KXIIHF` Who will win IIHF championship? — non-NHL hockey marker 'IIHF'
- skip `KXNCAAHOCKEYGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLLINDSAY` NHL Ted Lindsay Winner — ticker prefix KXNHL
- skip `KXKHL` KHL Champion — non-NHL hockey marker 'KHL'
- skip `KXWOMHOCKEY` Winter Olympics Men's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHL3PTOTAL` 3rd Period Total — ticker prefix KXNHL
- NHL  `KXCONNSMYTHE` Conn Smythe trophy — NHL trophy/futures marker
- NHL  `KXNHLSERIESTOTALGOAL` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHLSERIESGAMES` NHL Series Total Games — ticker prefix KXNHL
- NHL  `KXNHLTEAMTOTAL` NHL Team Goals Scored During Game — ticker prefix KXNHL
- skip `KXELH` ELH Champion — no NHL marker
- NHL  `KXNHLDRAFTTOP` Pro Hockey Top Pick — ticker prefix KXNHL
- NHL  `KXNHLPSEASONGOALS` Player Goals Scored in Season — ticker prefix KXNHL
- NHL  `KXNHLANYGOAL` Pro Hockey Goalscorer — ticker prefix KXNHL
- skip `KXDEL` DEL Champion — non-NHL hockey marker 'DEL '
- NHL  `KXNHLSERIES` NHL Series Winner — ticker prefix KXNHL
- skip `KXLIIGAGAME` Liiga Game — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHLPLAYOFFGOALS` NHL Playoffs Goal Leader (by Round) — ticker prefix KXNHL
- NHL  `KXNHLMENTION` NHL Announcer Mentions — ticker prefix KXNHL
- skip `KXWOMHOCKEYFIRSTGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLFIRSTGOAL` NHL First Goal — ticker prefix KXNHL
- NHL  `KXNHLEAST` Eastern Conference Championship — ticker prefix KXNHL
- NHL  `KXNHL3P` NHL 3rd Period Winner — ticker prefix KXNHL
- NHL  `KXNHL1STTEAM` All NHL First Team — ticker prefix KXNHL
- NHL  `KXNHLRICHARD` NHL Maurice "Rocket" Richard Trophy — ticker prefix KXNHL
- skip `KXSHLGAME` SHL Game — non-NHL hockey marker 'SHL'
- NHL  `KXTEAMSINSC` Teams in Stanley Cup — NHL trophy/futures marker
- NHL  `KXNHL2PSPREAD` 2nd Period Spread — ticker prefix KXNHL
- NHL  `KXNHLNEXTTEAM` NHL Next Team — ticker prefix KXNHL
- NHL  `KXNHLRETIRE` NHL Retire — ticker prefix KXNHL
- skip `KXWO-HOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLVEZINA` NHL Vezina Trophy — ticker prefix KXNHL
- skip `KXLIGMAGGAME` Ligue Magnus Game — no NHL marker
- NHL  `KXESPYNHL` BEST NHL PLAYER‬ — title mentions NHL
- skip `KXIIHFGAME` IIHF Game — non-NHL hockey marker 'IIHF'
- skip `KXPHLGAME` Polish Hockey Game — no NHL marker
- NHL  `KXNHLRECORDWORST` Worst NHL Record — ticker prefix KXNHL
- skip `KXNCAAHOCKEY` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXNEXTTEAMNHL` Next Team NHL — title mentions NHL
- skip `KXWOMHOCKEYGOAL` Olympic Hockey Goalscorer — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLSAVES` Pro Hockey Saves — ticker prefix KXNHL
- NHL  `KXNHLMVP` NHL Hart Memorial Trophy Winner — ticker prefix KXNHL
- skip `KXWOHOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLF10G` NHL Goal in First 10 Minutes — ticker prefix KXNHL
- NHL  `KXNBANHL` NBA + NHL Champion Combo — title mentions NHL
- NHL  `KXNHLPACIFIC` NHL Pacific Division Winner — ticker prefix KXNHL
- NHL  `KXNHLEXPANSION` NHL Expansion — ticker prefix KXNHL
- NHL  `KXNHLNORRIS` NHL James Norris Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLOT` NHL Overtime — ticker prefix KXNHL
- NHL  `KXNHL1PTOTAL` NHL 1st Period Total — ticker prefix KXNHL
- NHL  `KXNHLROSS` NHL Art Ross Trophy — ticker prefix KXNHL
- NHL  `KXNHL3PSPREAD` NHL 3rd Period Spread — ticker prefix KXNHL
- NHL  `KXNHL2PBTTS` NHL Both Teams to Score in 2nd Period — ticker prefix KXNHL
- NHL  `KXCANADACUP` Canada winning Stanley Cup — NHL trophy/futures marker
- NHL  `KXNHLSAVE` Goaltender Saves — ticker prefix KXNHL
- skip `KXNCAAH` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLSERIESSPREAD` NHL Series Game Spread — ticker prefix KXNHL
- skip `KXEARNINGSMENTIONHLT` HILTON — no NHL marker
- NHL  `KXNHL30COMEBACK` NHL 3-0 Series Comeback — ticker prefix KXNHL
- NHL  `KXNHLSERIESTOTALGOALS` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHLOVERTIME` NHL Overtime — ticker prefix KXNHL
- skip `KXWOMHOCKEYFGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLPLAYOFF` Playoff Qualifier — ticker prefix KXNHL
- NHL  `KXNHLPTS` Pro Hockey Points — ticker prefix KXNHL
- skip `KXIIHFCHAMP` IIHF World Championship winner — non-NHL hockey marker 'IIHF'
- NHL  `KXNHL1P` NHL 1st Period Winner — ticker prefix KXNHL
- NHL  `KXNHLHART` NHL Hart Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLPRICE` NHL Ticket Prices — ticker prefix KXNHL
- skip `KXDELGAME` DEL Game — non-NHL hockey marker 'DEL '
- skip `KXNCAAHGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLSEASONGOALS` Player to score X Goals in Season — ticker prefix KXNHL
- skip `KXWOWHOCKEY` Winter Olympics Women's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHL3PBTTS` NHL Both Teams to Score in 3rd Period — ticker prefix KXNHL
- NHL  `KXNHLNEXTGM` Next NHL GM — ticker prefix KXNHL
- NHL  `KXNHLSEASONPTS` NHL Season Point Totals — ticker prefix KXNHL
- NHL  `KXNHLADAMS` NHL Jack Adams Award — ticker prefix KXNHL
- skip `KXAHLGAME` AHL Game — non-NHL hockey marker 'AHL'
- skip `KXAHL` AHL Champion — non-NHL hockey marker 'AHL'
- skip `KXSHL` SHL Champion — non-NHL hockey marker 'SHL'
- skip `KXWOMHOCKEYTOTAL` Winter Olympics Men's Hockey Goal Total — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLSERIESOT` NHL Series Overtime — ticker prefix KXNHL
- NHL  `KXNHLWSTREAK` Longest NHL win streak in regular season — ticker prefix KXNHL
- skip `KXKHLGAME` KHL Game — non-NHL hockey marker 'KHL'
- skip `KXINTHOCKEY` International Hockey — no NHL marker
- skip `KXEUCHLGAME` Champions League Hockey — non-NHL hockey marker 'CHL'
- NHL  `KXNHL1PSPREAD` 1st Period Spread — ticker prefix KXNHL
- skip `KXWOMHOCKEYSPREAD` Winter Olympics Men's Hockey Spread — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLFINALSEXACT` NHL Championship Series Score — ticker prefix KXNHL
- NHL  `KXNHLSEASONPPTS` Season Player Points — ticker prefix KXNHL
- NHL  `KXNHLGOAL` NHL Goalscorer — ticker prefix KXNHL
- NHL  `KXNHLTOTAL` NHL Total Goals — ticker prefix KXNHL
- NHL  `KXNHLDRAFTPICK` Pro Hockey Draft Pick — ticker prefix KXNHL
- NHL  `KXNHL2OT` NHL Double Overtime — ticker prefix KXNHL
- NHL  `KXNHLCENTRAL` NHL Central Division Winner — ticker prefix KXNHL
- NHL  `KXNHL2PTOTAL` 2nd Period Total — ticker prefix KXNHL
- skip `KXELHGAME` ELH Game — no NHL marker
- NHL  `KXNHLCALDER` NHL Calder Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLMETROPOLITAN` NHL Metropolitan Division Winner — ticker prefix KXNHL
- NHL  `KXNHLPRES` NHL President's Trophy Winner — ticker prefix KXNHL
- NHL  `KXNHL4NATIONS` 4 nations face off — ticker prefix KXNHL
- NHL  `KXNHLAST` Pro Hockey Assists — ticker prefix KXNHL
- NHL  `KXNHLWINS` NHL wins  — ticker prefix KXNHL
- NHL  `KXNHLATLANTIC` NHL Atlantic Division Winner — ticker prefix KXNHL
- NHL  `KXNHLWEST` Western Conference Champion — ticker prefix KXNHL
- skip `KXNLGAME` National League Game — no NHL marker
- NHL  `KXNHL` Stanley Cup — ticker prefix KXNHL
- skip `KXNL` National League Champion — no NHL marker
- skip `KXWOMHOCKEYMVP` Men's Winter Olympics Hockey MVP — non-NHL hockey marker 'OLYMPIC'
