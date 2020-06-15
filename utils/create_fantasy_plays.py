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

from config import INPUT_DATA_LOC, OUTPUT_DATA_LOC, MIN_YR, MAX_YR, NEEDED_COLUMNS, MAX_WEEK


# -

def create_fantasy_plays():
    all_seasons_fantasy_plays = 0
            
    for yr in np.arange(MIN_YR, MAX_YR+1):\
        
        reg_pbp = pd.read_csv(INPUT_DATA_LOC +\
                              f'play_by_play_data/regular_season/reg_pbp_{yr}.csv')
        
        accepted_play_types = ['play', 'run']
        fantasy_plays = reg_pbp[reg_pbp['play_type'].isin(accepted_play_types)]
        
        fantasy_plays = fantasy_plays[NEEDED_COLUMNS]

        if type(all_seasons_fantasy_plays) is int:
            all_seasons_fantasy_plays = fantasy_plays
        else:
            all_seasons_fantasy_plays = pd.concat([all_seasons_fantasy_plays,
                                                   fantasy_plays])

    game_week_map = pd.read_csv(OUTPUT_DATA_LOC + 'game_week_map.csv')
    
    all_seasons_fantasy_plays = all_seasons_fantasy_plays.\
                                    merge(game_week_map,
                                          how='inner',
                                          on='game_id')
    
    weeks_considered = np.arange(1,MAX_WEEK+1)
    all_seasons_fantasy_plays = all_seasons_fantasy_plays[all_seasons_fantasy_plays['week'].isin(weeks_considered)]    
      
    all_seasons_fantasy_plays.to_csv(OUTPUT_DATA_LOC + 'fantasy_plays.csv', index=False)
    
    return all_seasons_fantasy_plays
