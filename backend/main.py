from helpers import *

player_id = name_to_id("LeBron James")
player_df = get_player_match_history(player_id)

prize_picks_projects = get_prizepicks_lines()
print(prize_picks_projects.head())

recent = get_5_10_hitrate(player_df, 21.5)