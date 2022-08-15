# Import Necessary Libaries
import urllib.request
import re
import pandas as pd
import os

# Load website HTML into workable form
url = 'https://baseballsavant.mlb.com/leaderboard/spin-direction-pitches?year=2022&min=1&sort=7&sortDir=desc&pitch_type=ALL&throws=&playerName=&team=&pov=Pit'
response = urllib.request.Request(url=url)
raw = urllib.request.urlopen(response) # raw contents
workable_form = str(raw.read()) # raw contents converted to string -- makes data workable with REGEX

# Narrow website data to only table data
data_list = re.findall(r'var leaderboardData.*}];\\n</script>', workable_form)
data_str = re.findall(r'{.*}', data_list[0])[0]

# Separate chunk of data into individual hitters
player_data = data_str.split('},{')

#Establish headers
headers = ['player_id', 'pitch_type', 'spin_axis']

# Initialize dataframe data as list of lists
data = []

for i in range(len(player_data)):

    player = player_data[i]

    # Pull player_id and pitch type information
    id_data = re.findall(r'[0-9]+-[A-Z]{2}', player)[0]
    player_id = int(re.findall(r'[0-9]+', id_data)[0])
    pitch_type = re.findall(r'[A-Z]{2}', id_data)[0]

    # Pull spin axis information
    axis_data = re.findall(r'movement_inferred_clock_label":"[0-9]+:[0-9]{2}', player)[0]
    axis = re.findall(r'[0-9].*', axis_data)[0]

    # Compile aspects into row and append row to dataframe
    data.append([player_id, pitch_type, axis])

# Initialize dataframe with data and headers
axis_characteristics = pd.DataFrame(data, columns = headers)

# Create columns for each pitch's spin axis
axis_characteristics = axis_characteristics.pivot(index='player_id', columns='pitch_type')

# create new column names
new_col_names = []
for col in axis_characteristics:
    new_col_name = col[1] + '_' + col[0]
    new_col_names.append(new_col_name)

# Change column names
axis_characteristics.columns = new_col_names
axis_characteristics.reset_index(inplace=True)

# Write dataframe to csv
cwd = os.getcwd()
path = cwd + "/axis.csv"
axis_characteristics.to_csv(path, index=False)