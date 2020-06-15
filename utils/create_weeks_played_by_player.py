# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import numpy as np
import sys
sys.path.append('/Users/joeday/Documents/Fantasy/')

from config import INPUT_DATA_LOC, OUTPUT_DATA_LOC


# -

def create_weeks_played():
    fantasy_plays = pd.read_csv(OUTPUT_DATA_LOC + 'fantasy_plays.csv')
    
    weeks_played = pd.concat([
            fantasy_plays[['rusher_player_id','week', 'season']].\
                drop_duplicates().\
                rename({'rusher_player_id':'player_id'}, axis=1),
            fantasy_plays[['receiver_player_id','week', 'season']].\
                drop_duplicates().\
                rename({'receiver_player_id':'player_id'}, axis=1),
            fantasy_plays[['passer_player_id','week', 'season']].\
                drop_duplicates().\
                rename({'passer_player_id':'player_id'}, axis=1),
            ]).\
            drop_duplicates().\
            groupby(['player_id', 'season']).\
            count().\
            reset_index()


    weeks_played.columns = ['player_id', 'season', 'games_played']
    
    weeks_played.to_csv(OUTPUT_DATA_LOC + 'weeks_played.csv', index=False)
    
    return weeks_played
