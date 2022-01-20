import pandas as pd
import numpy as np

def find_selected_player_comps(pCompAvg, chosenPlayerLoc):
    eligiblePlayerCompsList = []
    # For all data points in pCompAvg, copy them over to a list (eventually to be turned into a DataFrame) if the player of current iteration throws with the same hand as the selected player but is not the selected player
    # Note - the selected player would have a Similarity Score of 1 (identical) so there is no point in including them
    for row in pCompAvg.index:
        if ((pCompAvg.at[row,'hand'] == pCompAvg.at[chosenPlayerLoc,'hand']) and (pCompAvg.at[row, 'player_name'] != pCompAvg.at[chosenPlayerLoc, 'player_name'])):
            eligiblePlayerCompsList.append(pCompAvg.loc[row])
    eligiblePlayerComps = pd.DataFrame(eligiblePlayerCompsList)
    # For all eligible players, change each metric's value to the absolute value of the difference between the selected player's difference from average metric and the current iteration player's difference from average metric
    for row in eligiblePlayerComps.index:
        eligiblePlayerComps.loc[row,'ff_speed':'fs_RPz'] = abs(pCompAvg.loc[chosenPlayerLoc, 'ff_speed':'fs_RPz'] - eligiblePlayerComps.loc[row, 'ff_speed':'fs_RPz'])
    return(eligiblePlayerComps)