import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from constants import * 

def name_to_id(name: str) -> str:
    player = players.find_players_by_full_name(name)

    if player and len(player) > 0:
        return str(player[0]['id'])
    return None

def get_player_match_history(id: str) -> list:
    game_log = pd.DataFrame([])
    for season in SEASONS:
        season_game_log = playergamelog.PlayerGameLog(player_id=id, season=season)
        season_game_log_df = pd.DataFrame(season_game_log.get_data_frames()[0])[::-1]
        game_log = pd.concat([game_log, season_game_log_df], ignore_index=True)

    return game_log

def get_5_10_hitrate(game_log, line) -> dict:
    crossed = []
    wanted_games = game_log.tail(10)
    
    for _, game in wanted_games.iterrows():
        if game['PTS'] >= line:
            crossed.append(1)
        else:
            crossed.append(0)
            
    return {
        'last5': (crossed[-5:].count(1)/5),
        'last10': (crossed.count(1)/ 10)
    }

def get_head_to_head(game_log, opp) -> dict:
    return {}

    
        

