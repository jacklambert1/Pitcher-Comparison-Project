# Import Necessary Libaries
import urllib.request
import re
import pandas as pd
import os

# Load website HTML into workable form
url = 'https://baseballsavant.mlb.com/leaderboard/pitch-arsenal-stats?type=pitcher&pitchType=&year=2022&team=&min=1'
response = urllib.request.Request(url=url)
raw = urllib.request.urlopen(response) # raw contents
workable_form = str(raw.read()) # raw contents converted to string -- makes data workable with REGEX

# Narrow website data only to table information
data_list = re.findall(r'leaderboardData = .*];\\n\\n</script>\\n\\n', workable_form)
data_str = re.findall(r'{.*}', data_list[0])[0]

# Separate chunk of data into individual hitters
player_data = data_str.split('},{')

# Establish headers and data
headers = ['player_id', 'pitch_type', 'rv_per_100']
df_data = []

# Relevant Values: player_id: 4, pitch_type: 8, run_val_per_100: 42

player_id_num = 4
pitch_type_num = 8
run_val_per_100_num = 42

for i in range(len(player_data)):

    data = player_data[i].split(',')

    player_id = data[player_id_num].split(':')[1].replace('"', '')
    pitch_type = data[pitch_type_num].split(':')[1].replace('"', '')

    # Correct weird pitch naming
    if pitch_type == 'CUKC':
        pitch_type = 'CU'
    elif pitch_type == 'SIFT':
        pitch_type = 'SI'

    run_val_per_100 = data[run_val_per_100_num].split(':')[1].replace('"', '')

    row = [player_id, pitch_type, run_val_per_100]
    df_data.append(row)

# Create dataframe
run_value_data = pd.DataFrame(df_data, columns = headers)
run_value_data = run_value_data[run_value_data['pitch_type'] != 'FA']

# Pivot columns
run_value_data = run_value_data.pivot(index='player_id', columns='pitch_type')

new_col_names = []
for col in run_value_data:
    new_col_name = col[1] + '_' + col[0]
    new_col_names.append(new_col_name)

# Change column names
run_value_data.columns = new_col_names
run_value_data.reset_index(inplace=True)

# Write dataframe to csv
cwd = os.getcwd()
path = cwd + "/run_values.csv"
run_value_data.to_csv(path, index=False)