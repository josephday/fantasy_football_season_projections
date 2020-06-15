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


def create_game_week_map():
    
    game_week_map = 0
    
    for yr in np.arange(MIN_YR, MAX_YR+1):
        reg_games = pd.read_csv(
                        INPUT_DATA_LOC +\
                        f'games_data/regular_season/reg_games_{yr}.csv')
        if type(game_week_map) is int:
            game_week_map = reg_games[['game_id', 'week', 'season']]
        else:
            game_week_map = pd.concat([game_week_map,
                                       reg_games[['game_id', 'week', 'season']]])
    
    game_week_map.to_csv(OUTPUT_DATA_LOC + 'game_week_map.csv', index=False)
    
    return game_week_map
