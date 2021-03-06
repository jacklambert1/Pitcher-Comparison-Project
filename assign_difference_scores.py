import pandas as pd
import numpy as np

def assign_difference_scores(eligiblePlayerComps, differenceScores, pitchInfo, row, difScoreRow):
    # Iterating through all columns of 'pitchInfo' allows for all values for each specific pitch to be referenced and changed
    # Note - each pitch type is represented by column name and each attribute of pitch type is represented by index value
    # Note - in this function the values 0 (xx_speed), 1 (xx_spin), 2 (xx_xBreak), 3 (xx_zBreak), 4 (xx_RPx), 5 (xx_RPz), 6 (release_point), 7 (xx_comps), and 8 (xx_score) are referenced
    for column in pitchInfo:
        # Difference Score is an average of the absolute value of the difference between the selected player and all other players for all stats. Since not every player has data on 'xx_RPx', 'xx_RPz', and/or 'release_extension', the average is dependent on the number of comparisons they have
        if (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 7):
            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]] + eligiblePlayerComps.at[row, pitchInfo.at[4, column]] + eligiblePlayerComps.at[row, pitchInfo.at[5, column]] + eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]
        elif (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 6):
            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]] + eligiblePlayerComps.at[row, pitchInfo.at[4, column]] + eligiblePlayerComps.at[row, pitchInfo.at[5, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]
        elif (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 5):
            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]] + eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]
        elif (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 4):
            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]
    return(differenceScores)