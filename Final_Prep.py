import pandas as pd
import os

# Read in CSVs
cwd = os.getcwd()
master_path = cwd + "/master.csv"
scores_path = cwd + "/scores.csv"
master = pd.read_csv(master_path)
scores = pd.read_csv(scores_path)

# Initialize lists for number of comparison players with scores under 50, the closest score value, and closest score unique_id
n_under_50 = []
closest = []
closest_id = []

# Count number of scores under 50 for each pitch, closest score value, and closest score id
for row in master.index:
    
    relevant_scores = scores[scores['unique_id'] == master.at[row, 'unique_id']]

    n_under_50.append(len(relevant_scores[relevant_scores['score'] < 50]))

    min_ind = relevant_scores['score'].idxmin()
    closest.append(relevant_scores.at[min_ind, 'score'])
    closest_id.append(relevant_scores.at[min_ind, 'comp_id'])
    
# Set new columns equal to lists
master['scores_under_50'] = n_under_50
master['closest_score'] = closest
master['closest_id'] = closest_id

# Initialize uniquness list
uniqueness = []

# Set uniquness accordingly
for pitch in master.index:
    
    if master.at[pitch, 'scores_under_50'] < 1: # none under 50
        uniqueness.append('Unicorn')
    elif master.at[pitch, 'scores_under_50'] < 5: # 1-4 under 50
        uniqueness.append('Extremely Rare')
    elif master.at[pitch, 'scores_under_50'] < 13: # 5-12 under 50 
        uniqueness.append('Very Rare')
    elif master.at[pitch, 'scores_under_50'] < 29: # 13-28 under 50
        uniqueness.append('Rare')
    elif master.at[pitch, 'scores_under_50'] < 61: # 29-60 under 50
        uniqueness.append('Uncommon')
    else: # more than 60 under 50
        uniqueness.append('Common')

# Set column equal to list
master['uniqueness'] = uniqueness

# Writes master and scores to csv
master.to_csv(master_path, index=False)