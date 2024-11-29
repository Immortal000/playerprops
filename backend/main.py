from helpers import *

player_id = name_to_id("LeBron James")
player_df = get_player_match_history(player_id)

recent = get_5_10_hitrate(player_df, 21.5)
print(recent)
