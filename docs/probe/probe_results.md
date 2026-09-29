# Source probe

probed 2026-09-29T04:17:53+00:00 for date 2026-09-29

| name | status | ms | bytes | kind | note |
|---|---:|---:|---:|---|---|
| nhl_schedule_date | 200 | 176 | 84310 | json | nextStartDate, previousStartDate, gameWeek, oddsPartners, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDa |
| nhl_schedule_now | 200 | 89 | 84310 | json | nextStartDate, previousStartDate, gameWeek, oddsPartners, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDa |
| nhl_score_now | 200 | 75 | 18390 | json | prevDate, currentDate, nextDate, gameWeek, oddsPartners, games |
| nhl_score_date | 200 | 38 | 18390 | json | prevDate, currentDate, nextDate, gameWeek, oddsPartners, games |
| nhl_standings_now | 200 | 77 | 51555 | json | wildCardIndicator, standingsDateTimeUtc, standings |
| nhl_roster_tor | 200 | 137 | 10390 | json | forwards, defensemen, goalies |
| nhl_club_schedule_tor | 200 | 125 | 188381 | json | previousSeason, currentSeason, clubTimezone, clubUTCOffset, games |
| nhl_club_schedule_tor_2025 | 200 | 163 | 184101 | json | previousSeason, currentSeason, nextSeason, clubTimezone, clubUTCOffset, games |
| nhl_club_stats_tor | 200 | 131 | 17323 | json | season, gameType, skaters, goalies |
| nhl_boxscore_final_2025 | 200 | 283 | 13529 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_landing_final_2025 | 200 | 428 | 11355 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_pbp_final_2025 | 200 | 238 | 146277 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_right_rail_2025 | 200 | 385 | 4550 | json | seasonSeries, seasonSeriesWins, gameInfo, gameVideo, linescore, shotsByPeriod, teamGameStats, gameReports |
| nhl_boxscore_ot_sample | 200 | 273 | 13147 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_schedule_calendar | 200 | 93 | 12704 | json | endDate, nextStartDate, previousStartDate, startDate, teams |
| nhl_season_list | 200 | 66 | 982 | json | l, i, s, t, [, 1, 0, 9 |
| nhl_stats_team | 200 | 172 | 6664 | json | data, total |
| nhl_stats_team_summary_prev | 200 | 112 | 16854 | json | data, total |
| nhl_stats_team_summary_cur | 200 | 79 | 21 | json | data, total |
| nhl_stats_goalie_summary_prev | 200 | 131 | 38937 | json | data, total |
| nhl_stats_goalie_summary_cur | 200 | 73 | 21 | json | data, total |
| nhl_stats_season | 200 | 112 | 65173 | json | data, total |
| nhl_stats_game_prev | 200 | 113 | 1259 | json | data, total |
| mp_teams_2025 | 200 | 544 | 99689 | csv | team, season, name, team, position, situation, games_played, xGoalsPercentage |
| mp_teams_2026 | 404 | 962 | 196 | html | HTTPError 404 |
| mp_goalies_2025 | 200 | 105 | 93386 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_goalies_2026 | 200 | 894 | 489 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_skaters_2025 | 200 | 150 | 400000 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_lines_2025 | 200 | 175 | 400000 | csv | lineId, season, name, team, position, situation, games_played, icetime |
| mp_all_teams_gbg | 200 | 189 | 600000 | csv | team, season, name, gameId, playerTeam, opposingTeam, home_or_away, gameDate |
| mp_team_gbg_tor | 200 | 158 | 400000 | csv | team, season, name, gameId, playerTeam, opposingTeam, home_or_away, gameDate |
| mp_shots_2024_zip_head | 404 | 92 | 0 |  | HTTPError 404 |
| mp_shots_2025_zip_head | 404 | 84 | 0 |  | HTTPError 404 |
| mp_shots_pt_2024_head | 200 | 157 | 0 |  |  |
| mp_shots_pt_2025_head | 200 | 48 | 0 |  |  |
| mp_shots_pt_2007_2023_head | 404 | 126 | 0 |  | HTTPError 404 |
| mp_predictions_page | 200 | 70 | 20000 | html |  |
| espn_nhl_scoreboard | 200 | 153 | 72293 | json | leagues, events, provider |
| espn_nhl_teams | 200 | 197 | 136961 | json | sports |
| dailyfaceoff_goalies | 200 | 124 | 30000 | html |  |
| dailyfaceoff_goalies_date | 200 | 96 | 30000 | html |  |
| rotowire_goalies | 200 | 514 | 30000 | html |  |
| nhl_injuries_espn | 200 | 80 | 1208735 | json | timestamp, status, season, injuries |
| kalshi_api_exchange_status | 200 | 53 | 667 | json | exchange_active, exchange_index_statuses, intra_exchange_transfers_active, trading_active |
| kalshi_api_series_sports | 200 | 236 | 3000000 | json-invalid |  |
| kalshi_api_series_kxnhlgame | 200 | 47 | 1569 | json | series |
| kalshi_api_markets_kxnhlgame_open | 200 | 58 | 157584 | json | cursor, markets |
| kalshi_api_markets_kxnhlgame_unopened | 200 | 122 | 27 | json | cursor, markets |
| kalshi_api_markets_kxnhlgame_settled | 200 | 59 | 99699 | json | cursor, markets |
| kalshi_api_events_kxnhlgame | 200 | 90 | 210319 | json | cursor, events, milestones |
| kalshi_api_markets_kxnhlspread_open | 200 | 84 | 124059 | json | cursor, markets |
| kalshi_api_markets_kxnhltotal_open | 200 | 66 | 203872 | json | cursor, markets |
| kalshi_api_filters_by_sport | 200 | 51 | 17500 | json | filters_by_sports, sport_ordering |
| kalshi_external_api_exchange_status | 200 | 110 | 667 | json | exchange_active, exchange_index_statuses, intra_exchange_transfers_active, trading_active |
| kalshi_external_api_series_sports | 200 | 326 | 3000000 | json-invalid |  |
| kalshi_external_api_series_kxnhlgame | 200 | 87 | 1569 | json | series |
| kalshi_external_api_markets_kxnhlgame_open | 200 | 96 | 157585 | json | cursor, markets |
| kalshi_external_api_markets_kxnhlgame_unopened | 200 | 82 | 27 | json | cursor, markets |
| kalshi_external_api_markets_kxnhlgame_settled | 200 | 94 | 99699 | json | cursor, markets |
| kalshi_external_api_events_kxnhlgame | 200 | 122 | 210319 | json | cursor, events, milestones |
| kalshi_external_api_markets_kxnhlspread_open | 200 | 121 | 124059 | json | cursor, markets |
| kalshi_external_api_markets_kxnhltotal_open | 200 | 125 | 203872 | json | cursor, markets |
| kalshi_external_api_filters_by_sport | 200 | 71 | 17500 | json | filters_by_sports, sport_ordering |
