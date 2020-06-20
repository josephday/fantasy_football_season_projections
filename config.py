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
INPUT_DATA_LOC = '../data/nflscrapR-data/'
OUTPUT_DATA_LOC = '../data/features/'
MIN_YR = 2009
MAX_YR = 2019
MAX_WEEK = 16

TEAM_ABBR_RENAME = {'SD': 'LAC',
                   'LA': 'LAR',
                   'STL': 'LAR',
                   'OAK': 'LV',
                   'JAC': 'JAX'}

NEEDED_COLUMNS = ['play_id',
                  'game_id',
                  'game_date',
                  'posteam',
                  'defteam',
                  'yardline_100',
                  'play_type',
                  'yards_gained', 
                  'air_yards',
                  'yards_after_catch',
                  'run_gap',
                  'run_location',
                  'pass_touchdown', 
                  'rush_touchdown',
                  'rush_attempt',
                  'pass_attempt',
                  'sack',
                  'fumble',
                  'interception',
                  'complete_pass',
                  'passer_player_id',
                  'passer_player_name',
                  'receiver_player_id',
                  'receiver_player_name', 
                  'rusher_player_id',
                  'rusher_player_name']
