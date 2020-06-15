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

def create_position_map():
    
    position_map = 0
    
    for yr in np.arange(MIN_YR, MAX_YR+1):
        positions = pd.read_csv(
                        INPUT_DATA_LOC +\
                        f'roster_data/regular_season/reg_roster_{yr}.csv')
        if type(position_map) is int:
            position_map = positions[['season', 'gsis_id', 'position']]
        else:
            position_map = pd.concat([position_map,
                                      positions[['season', 'gsis_id', 'position']]])
            
    position_map.rename({'gsis_id':'player_id'}, axis=1, inplace=True)
    
    position_map.to_csv(OUTPUT_DATA_LOC + 'position_map.csv', index=False)
    
    return position_map
