# Import Necessary Libaries
import urllib.request
import re
import pandas as pd
import os

# Load website HTML into workable form
url = 'https://baseballsavant.mlb.com/leaderboard/custom?year=2022&type=pitcher&filter=&sort=17&sortDir=desc&min=10&selections=ff_avg_speed,ff_avg_spin,ff_avg_break_x,ff_avg_break_z,sl_avg_speed,sl_avg_spin,sl_avg_break_x,sl_avg_break_z,ch_avg_speed,ch_avg_spin,ch_avg_break_x,ch_avg_break_z,cu_avg_speed,cu_avg_spin,cu_avg_break_x,cu_avg_break_z,si_avg_speed,si_avg_spin,si_avg_break_x,si_avg_break_z,fc_avg_speed,fc_avg_spin,fc_avg_break_x,fc_avg_break_z,fs_avg_speed,fs_avg_spin,fs_avg_break_x,fs_avg_break_z,kn_avg_speed,kn_avg_spin,kn_avg_break_x,kn_avg_break_z,&chart=false&x=ff_avg_speed&y=ff_avg_speed&r=no&chartType=beeswarm'
response = urllib.request.Request(url=url)
raw = urllib.request.urlopen(response) # raw contents
workable_form = str(raw.read()) # raw contents converted to string -- makes data workable with REGEX

# Narrow website data only to table information
data_list = re.findall(r'var data.*\\n\\n<div', workable_form)
data_str = re.findall(r'{.*}', data_list[0])[0]

# necessary list elements: 3, 84, 90, 92, 94-98, 106-108, 110-114, 121-124, 126-130, 137-140, 142-146, 153-156, 158-162, 169-172, 174-178, 185-188, 190-194, 201-204, 206-210, 217-220, 374

# Separate chunk of data into individual hitters
player_data = data_str.split('},{')

# Take first player to pull headers
header_data = player_data[0].split(',"')
headers = []

player_id_num = 3 # element of list corresponding to player id
player_name_num = 501 # element of list corresponding to player name
player_hand_num = 90 # element of list corresponding to player hand
player_total_pitches_num = 92 # element of lsit correpsonding to total pitches thrown

# element of list corresponding to player outcome stats -- used for regression model later
player_era_num = 374 
player_kpct_num = 57
player_barrelpct_num = 60
player_xwoba_num = 77

# append player id and name to list of headers
headers.append(header_data[player_id_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_name_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_hand_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_total_pitches_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_era_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_kpct_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_barrelpct_num].split(':')[0].replace('"', ''))
headers.append(header_data[player_xwoba_num].split(':')[0].replace('"', ''))


unique_pitches = 8 # number of pitches there is data for
unique_attributes = 5 # number of attributes for each pitch
unique_attributes2 = 3 # number of 2nd batch of attrbibutes for each pitch
first_loc = 93 # element of list corresponding to first pitch attribute

val = first_loc # initialize val to first location

# Iterate through all attributes of all pitches
for pitch in range(unique_pitches):
    for i in range(unique_attributes):
        val += 1

        # append individual headers to list of headers
        header = header_data[val].split(':')[0].replace('"', '')
        headers.append(header)

    val += 7
    for i in range(unique_attributes2):
        val += 1

        # append individual headers to list of headers
        header = header_data[val].split(':')[0].replace('"', '')
        headers.append(header)

    val += 1

# initialize list to create list of lists for dataframe
data = []

# iterate through every individual pitcher
for player in range(len(player_data)):

    row = []
    individual_data = player_data[player].split(',"') # initialize specific player

    # Append player id and name to row list
    row.append(individual_data[player_id_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_name_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_hand_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_total_pitches_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_era_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_kpct_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_barrelpct_num].split(':')[1].replace('"', ''))
    row.append(individual_data[player_xwoba_num].split(':')[1].replace('"', ''))

    val = first_loc # initialize val to first_loc

    # Iterate through all attributes of all pitches
    for pitch in range(unique_pitches):
        for i in range(unique_attributes):
            val += 1

            # append individual attributes to row
            row.append(individual_data[val].split(':')[1].replace('"', ''))
        
        val += 7
        for i in range(unique_attributes2):
            val += 1
            
            # append individual attributes to row
            row.append(individual_data[val].split(':')[1].replace('"', ''))

        val += 1

    # add row to dataframe data
    data.append(row)

# Create dataframe
pitch_characteristics = pd.DataFrame(data, columns = headers)

# Write dataframe to csv
cwd = os.getcwd()
path = cwd + "/pitch_characteristics.csv"
pitch_characteristics.to_csv(path, index=False)