from datetime import datetime
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from constants import * 
import json

def get_prizepicks_lines():
    DATE = f"{datetime.now().strftime('%m-%d-%Y')}"

    with open(f"./data/{DATE}.json", encoding='utf-8') as prize_projections:
        data = json.load(prize_projections)

    # Create main DataFrame with projections
    df = pd.json_normalize(
        data['data'],
        sep='.',
        meta=[
            'attributes.line_score',
            'attributes.start_time',
            'attributes.stat_type',
            ['relationships', 'new_player', 'data', 'id'],
            ['relationships', 'league', 'data', 'id']
        ]
    )

    # Create DataFrame for player information from included section
    players_df = pd.json_normalize(
        data['included'],
        sep='.',
        meta=[
            'id',
            'attributes.name'
            'attributes.league'
        ]
    )

    # Rename columns
    df = df.rename(columns={
        'attributes.line_score': 'line_score',
        'attributes.start_time': 'start_time',
        'attributes.stat_type': 'stat_type',
        'relationships.new_player.data.id': 'player_id',
        'relationships.league.data.id': 'league_id'
    })

    players_df = players_df.rename(columns={
        'attributes.name': 'player_name',
        'attributes.league': 'league'
    })

    # Merge the DataFrames on player_id
    df = df.merge(
        players_df[['id', 'player_name', 'league']], 
        left_on='player_id', 
        right_on='id'
    )

    # Select only the columns we want
    return df[df["league"] == "NBA"][['line_score', 'start_time', 'stat_type', 'player_id', 'league_id', 'player_name', 'league']]

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

    
        

