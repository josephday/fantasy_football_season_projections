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
sys.path.append('/Users/joeday/Documents/Fantasy/fantasy_football_season_projections')

from config import INPUT_DATA_LOC, OUTPUT_DATA_LOC, MIN_YR, MAX_YR, TEAM_ABBR_RENAME

def create_roster_map():
    
    roster_map = 0
    
    for yr in np.arange(MIN_YR, MAX_YR+1):
        rosters = pd.read_csv(
                        INPUT_DATA_LOC +\
                        f'roster_data/regular_season/reg_roster_{yr}.csv')
        if type(roster_map) is int:
            roster_map = rosters[['season', 'gsis_id', 'team']]
        else:
            roster_map = pd.concat([roster_map,
                                    rosters[['season', 'gsis_id', 'team']]])
            
    roster_map.rename({'gsis_id':'player_id'}, axis=1, inplace=True)
    
    roster_map['team'] = roster_map['team'].map(TEAM_ABBR_RENAME).fillna(roster_map['team'])
    
    roster_map.to_csv(OUTPUT_DATA_LOC + 'roster_map.csv', index=False)
    
    return roster_map
