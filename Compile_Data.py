# Import necessary libraries
import pandas as pd
import numpy as np
import os

def load_arsenals(data, pitches):
    
    # For each player, if that ptcher has a velocity value for each pitch then add that pitch to their arsenal
    for player in data.index:
        for pitch in pitches:
            test_str = pitch + '_avg_speed'
            if not np.isnan(data.at[player, test_str]):
                data.at[player, 'arsenal'].append(pitch)

    return data

def convert_spin_axis(spin_axis):

    # Split the spin axis time format to hour and minute value
    axis = str(spin_axis).split(':')
    hour = float(axis[0])
    min = float(axis[1])

    # Make starting time 0
    if hour == 12:
        hour = 0

    # Convert time to a degree value that can be manipulated
    new_axis = hour * 30 + min * .5

    # Flip degrees to go from 0-360 to -180-180
    if new_axis > 180:
        new_axis -= 360

    return new_axis

def make_new_row(player_data, pitch, pitch_translations):

    spin_axis = player_data[pitch.upper() + '_spin_axis']

    # If the type of the axis is a string then convert the spin axis to degrees
    if isinstance(spin_axis, str):
        degrees_spin_axis = convert_spin_axis(spin_axis)
    else:
        degrees_spin_axis = 0

    # Add image_url value based on formatted url
    image_url = 'https://img.mlbstatic.com/mlb-photos/image/upload/w_1000,q_100/v1/people/' + str(player_data['player_id']) + '/headshot/silo/current'

    # Add non-pitch specific data to row
    new_row = [pitch + '-' + str(player_data['player_id']), player_data['player_id'], player_data['player_name'].replace('\\', ''), player_data['pitch_hand'], pitch, pitch_translations[pitch], image_url, player_data[pitch.upper() + '_rv_per_100'], player_data['p_era'], player_data['k_percent'], player_data['barrel_batted_rate'], player_data['xwoba']]

    # Add pitch specific data to row
    new_row.append(player_data['n'] * player_data['n_' + pitch])
    new_row.append(player_data[pitch + '_avg_speed'])
    new_row.append(player_data[pitch + '_avg_spin'])
    new_row.append(player_data[pitch + '_avg_break_x'])
    new_row.append(player_data[pitch + '_avg_break_z'])
    new_row.append(spin_axis)
    new_row.append(degrees_spin_axis)
    new_row.append(player_data[pitch + '_rel_x'])
    new_row.append(player_data[pitch + '_rel_z'])
    new_row.append(60.5 - player_data[pitch + '_rel_y'])

    return new_row

# Read in CSVs
cwd = os.getcwd()
pitch_characteristics_path = cwd + "/pitch_characteristics.csv"
axis_path = cwd + "/axis.csv"
run_values_path = cwd + "/run_values.csv"

pitch_characteristics = pd.read_csv(pitch_characteristics_path)
axis = pd.read_csv(axis_path)
run_values = pd.read_csv(run_values_path)

# Merge datasets
all_data = pitch_characteristics.merge(axis, on='player_id', how='left')
all_data = all_data.merge(run_values, on='player_id', how='left')

# Initialize list of different pitches
pitches = ['ff', 'sl', 'ch', 'cu', 'si', 'fc', 'fs', 'kn']
pitch_translations = {'ff': 'Fourseam Fastball', 'sl': 'Slider', 'ch': 'Changeup', 'cu': 'Curveball', 'si': 'Sinker', 'fc': 'Cutter', 'fs': 'Splitter', 'kn': 'Knuckleball'}

# Initialize arsenal as empty list
all_data['arsenal'] = all_data.apply(lambda x: [], axis=1)

# Iterate through all players and load arsenals based on if there is an avg speed for each pitch type 
all_data = load_arsenals(all_data, pitches)

# Create new dataframe headers and data
new_cols = ['unique_id', 'player_id', 'player_name', 'hand', 'pitch_id', 'pitch_name', 'image_url', 'run_value_per_100', 'era', 'k%', 'barrel%', 'xwoba', 'total_pitches', 'velo', 'spin_rate', 'x_break', 'z_break', 'spin_axis', 'workable_spin_axis', 'rpx', 'rpz', 'extension']
data = []

# Fill in rows of new dataframe with each row corresponding to a player and a specific pitch and the characteristics of that pitch
for player in all_data.index:
    player_data = all_data.loc[player]
    for pitch in player_data['arsenal']:
        data.append(make_new_row(player_data, pitch, pitch_translations))

# Initialize revised_data dataframe given data and columns
revised_data = pd.DataFrame(data, columns = new_cols)
# Drop all rows where not all pitch characteristics are present
master = revised_data.dropna()

# Write dataframes to csv
path = cwd + "/master.csv"
master.to_csv(path, index=False)