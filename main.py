# Import necessary libraries
import pandas as pd
import numpy as np

# Read in data of MLB pitcher's statsitics from 2021 season
pComps = pd.read_csv('https://raw.githubusercontent.com/jacklambert1/Pitcher-Comparison-Project/main/2021_pitcher_data.csv')
pCompAvg = pComps.copy()

# Initialize DataFrame with columns of every different pitch type monitored in 2021 season and rows of chosen comparison statistics
# Since DataFrames contain indexing this DataFrame will be accessed relative to column name (for pitch type) and index value (for attribute for that pitch type)
# Note - 'xx_comps' and 'xx_score' are not a part of the original data set, but will have values relative to individual pitch so are included in the creation of DataFrame
fourseam = ['ff_speed', 'ff_spin', 'ff_xBreak', 'ff_zBreak', 'ff_RPx', 'ff_RPz', 'release_extension', 'ff_comps', 'ff_score']
cutter = ['fc_speed', 'fc_spin', 'fc_xBreak', 'fc_zBreak', 'fc_RPx', 'fc_RPz', 'release_extension', 'fc_comps', 'fc_score']
sinker = ['si_speed', 'si_spin', 'si_xBreak', 'si_zBreak', 'si_RPx', 'si_RPz', 'release_extension', 'si_comps', 'si_score']
splitter = ['fs_speed', 'fs_spin', 'fs_xBreak', 'fs_zBreak', 'fs_RPx', 'fs_RPz', 'release_extension', 'fs_comps', 'fs_score']
slider = ['sl_speed', 'sl_spin', 'sl_xBreak', 'sl_zBreak', 'sl_RPx', 'sl_RPz', 'release_extension', 'sl_comps', 'sl_score']
curveball = ['cu_speed', 'cu_spin', 'cu_xBreak', 'cu_zBreak', 'cu_RPx', 'cu_RPz', 'release_extension', 'cu_comps', 'cu_score']
changeup = ['ch_speed', 'ch_spin', 'ch_xBreak', 'ch_zBreak', 'ch_RPx', 'ch_RPz', 'release_extension', 'ch_comps', 'ch_score']
pitchInfo = pd.DataFrame(list(zip(fourseam, cutter, sinker, splitter, slider, curveball, changeup)), 
                         columns = ['Four Seam Fastball', 'Cutter', 'Sinker', 'Splitter', 'Slider', 'Curveball', 'Changeup'])

# Takes the average for each statistic of data set for all right handed pitchers and all left handed pitchers
RHPaverages = find_averages(pComps, 'R')
LHPaverages = find_averages(pComps, 'L')

# Changes all values of original data set to the percent difference between original value and league average for each player's throwing hand
pCompAvg = compare_vs_averages(pCompAvg, RHPaverages, LHPaverages)

# Prompts the user to select a pitcher and continues to do so until they enter a valid pitcher name (when this is done, chosenPlayerLoc changes from -1 to whichever index value the valid player is in the pComps DataFrame)
chosenPlayerLoc = -1
while (chosenPlayerLoc == -1):
    chosenPlayerLoc = find_selected_player(pComps, chosenPlayerLoc)

# Creates new DataFrame full of data of the absolute value of the difference (in percent difference from average) for all pitchers that throw with same hand as selected pitcher
eligiblePlayerComps = find_selected_player_comps(pCompAvg, chosenPlayerLoc)

# Adds 'xx_comps' column in 'eligiblePlayerComps' DataFrame which represents number of comparisons possible between selected player and each other eligible player (same throwing hand)
for column in pitchInfo:
    eligiblePlayerComps[pitchInfo.at[7, column]] = np.nan

# Fills in the 'xx_comps' column in 'eligiblePlayerComps' DataFrame with minimum of either 4 comparisons (every player has data on speed, spin, xBreak, and zBreak), 5 comparisons (some players are missing data on RPx and RPz), 6 comparisons (some players are missing data on release_extension), or 7 comparisons (all possible data is present)
for row in eligiblePlayerComps.index:
    eligiblePlayerComps = assign_comp_vals(eligiblePlayerComps, pitchInfo, row)

# Initialize DataFrame to represent the Difference Scores of each player (Difference Score is calculated by the average difference between the percent difference from average there is between selected player and all other players in the data set for each stat)
# Note - the lower the Difference Score the more similar the pitcher is
nameData = eligiblePlayerComps['player_name'].to_list()
ffScoreData = [np.nan] * len(eligiblePlayerComps.index)
slScoreData = [np.nan] * len(eligiblePlayerComps.index)
chScoreData = [np.nan] * len(eligiblePlayerComps.index)
cuScoreData = [np.nan] * len(eligiblePlayerComps.index)
siScoreData = [np.nan] * len(eligiblePlayerComps.index)
fcScoreData = [np.nan] * len(eligiblePlayerComps.index)
fsScoreData = [np.nan] * len(eligiblePlayerComps.index)
differenceScores = pd.DataFrame(list(zip(nameData, ffScoreData, slScoreData, chScoreData, cuScoreData, siScoreData, fcScoreData, fsScoreData)), 
                                columns = ['player_name', 'ff_score', 'sl_score', 'ch_score', 'cu_score', 'si_score', 'fc_score', 'fs_score'])

# Fills in the Difference Score for each player and each pitch
difScoreRow = 0
for row in eligiblePlayerComps.index:
    differenceScores = assign_difference_scores(eligiblePlayerComps, differenceScores, pitchInfo, row, difScoreRow)
    difScoreRow += 1

# Prints the conclusions from the program: which player's are most similar to the selected player for each pitch in the selected player's repertoire
# Note - the value that is printed is the Similarity Score (1 - Difference Score) not the Difference Score -- this is becuase it is  easier to think about the Similarity Score as 1 meaning the pitchers have the exact same metrics, rather than the Difference Score as 0 meaning they have no difference in their metrics
nComps = 3 # nComps can change based on how many similar pitchers the user wants to see (ex: right now the top 3 for each pitch are displayed)
print(pComps.at[chosenPlayerLoc, 'player_name'], 'Pitch Repertoire:')
print_results(differenceScores, pComps, pitchInfo, chosenPlayerLoc, nComps)