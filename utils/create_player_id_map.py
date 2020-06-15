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

from config import INPUT_DATA_LOC, OUTPUT_DATA_LOC, MIN_YR, MAX_YR

def create_player_id_map():
    
    player_id_map = 0
    
    for yr in np.arange(MIN_YR, MAX_YR+1):
        rosters = pd.read_csv(
                        INPUT_DATA_LOC +\
                        f'roster_data/regular_season/reg_roster_{yr}.csv')
        if type(player_id_map) is int:
            player_id_map = rosters[['gsis_id', 'full_player_name']]
        else:
            player_id_map = pd.concat([player_id_map,
                                       rosters[['gsis_id', 'full_player_name']]])
            
    player_id_map.rename({'gsis_id':'player_id'}, axis=1, inplace=True)
    player_id_map.reset_index(drop=True, inplace=True)
    player_id_map.drop_duplicates(inplace=True)
    
    player_id_map.to_csv(OUTPUT_DATA_LOC + 'player_id_map.csv', index=False)
    
    return player_id_map
