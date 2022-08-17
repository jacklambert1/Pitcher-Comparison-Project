import pandas as pd
import os
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

def find_multipliers(master, predictors):

    # Split data into predictors and the value being predicted
    x = master[predictors]
    y = master['run_value_per_100']

    # Establish dictionary with value being list of feature importances for each of 100 trials of xgboost model
    importances = {'velo': [], 'spin_rate': [], 'x_break': [], 'z_break': [], 'workable_spin_axis': [], 'rpx': [], 'rpz': [], 'extension': []}

    # Run 100 iterations of model
    for i in range(100):

        # Split data into train and test set
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Run regresion
        xgb = XGBRegressor(n_estimators=100)
        xgb.fit(x_train, y_train)

        # Add feature importance to list
        for predictor_val in range(len(predictors)):
            importances[predictors[predictor_val]].append(xgb.feature_importances_[predictor_val] * 100.0)

    # Create dictionary for multipliers for each feature
    multipliers = {}

    # Initialize multiplier by average importance for 100 trials
    for predictor in predictors:
        multipliers[predictor] = sum(importances[predictor]) / len(importances[predictor])

    # Takes total sum of all feature multipliers
    total_sum = sum(multipliers.values())

    # Change multipliers to add up to 100
    for predictor in predictors:
        multipliers[predictor] = multipliers[predictor] / total_sum

    return multipliers

def fill_out_scores(data, master, multipliers, rhp_std, lhp_std):

    # Iterate through all pitches
    for player in master.index:
        
        # Extract unique ID and pitch type of current pitch 
        unique_id = master.at[player, 'unique_id']
        pitch = master.at[player, 'pitch_id']
        hand = master.at[player, 'hand']

        if hand == 'R':
            std = rhp_std
        else:
            std = lhp_std
        
        # Determine whether comparisons will be with R or L filters
        comp_data = master[master['hand'] == hand]
        comp_data = comp_data[comp_data['player_id'] != master.at[player, 'player_id']]

        # Iterate through all eligible comparison players
        for comp_player in comp_data.index:

            # Extract unique ID of comparison player
            comp_id = comp_data.at[comp_player, 'unique_id']

            # Compute final score by adding up the difference in z scores multiplied by the multiplier
            score = 0
            for attribute in multipliers:
                difference = abs(master.at[player, attribute] - comp_data.at[comp_player, attribute]) / std[attribute]
                ind_score = difference * multipliers[attribute]
                score += ind_score

            # Add data to dataset
            data.append([unique_id, pitch, hand, comp_id, score])

    return data

# Read in CSVs
cwd = os.getcwd()
master_path = cwd + "/master.csv"
master = pd.read_csv(master_path)

# Initialize dataframes to contain information on the average/std characteristics for RHPs, LHPs, and all pitchers (found via absolute value of x_break, rpx, and workable_spin_axis)
comp_titles = ['velo', 'spin_rate', 'x_break', 'z_break', 'workable_spin_axis', 'rpx', 'rpz', 'extension']

# Establish multipliers off of average feature importance of 100 runs of  XGB Model based using comp_titles to predict RV per 100
multipliers = find_multipliers(master, comp_titles)

# Establish standard deviations
rhp_std = master[master['hand'] == 'R'][comp_titles].std()
lhp_std = master[master['hand'] == 'L'][comp_titles].std()

# Create list of data with comarison scores as dataframe
data = []
scores = fill_out_scores(data, master, multipliers, rhp_std, lhp_std)
scores = pd.DataFrame(data, columns = ['unique_id', 'pitch_id', 'hand', 'comp_id', 'score'])

# Write dataframe to csv
path = cwd + "/scores.csv"
scores.to_csv(path, index=False)
