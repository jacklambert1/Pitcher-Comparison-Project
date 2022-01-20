import pandas as pd
import numpy as np

def print_results(differenceScores, pComps, pitchInfo, chosenPlayerLoc, nComps):
    # Iterating through all columns of 'pitchInfo' allows for all values for each specific pitch to be referenced and changed
    # Note - each pitch type is represented by column name and each attribute of pitch type is represented by index value
    # Note - in this function the values 0 (xx_speed) and 8 (xx_score) are referenced
    for column in pitchInfo:
        if (np.isnan(pComps.at[chosenPlayerLoc, pitchInfo.at[0, column]]) == False): # only print a pitch name and similar pitchers if the selected pitcher throws that pitch (shown by the speed of that pitch being a numeric value)
            print(column)
            print('   Most similar pitches:')
            differenceScores.sort_values(pitchInfo.at[8, column], inplace = True) # Sorts values in 'differenceScores' from most similar to least similar for current pitch iteration
            differenceScores.reset_index(drop = True, inplace = True)
            for i in range(nComps):
                print('    ', differenceScores.at[i, 'player_name'], '-- Similarity Score:', round(1 - differenceScores.at[i, pitchInfo.at[8, column]], 3)) # 1 - Difference Score = Similarity Score