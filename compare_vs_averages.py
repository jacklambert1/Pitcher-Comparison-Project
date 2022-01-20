def compare_vs_averages(pCompAvg, RHPaverages, LHPaverages):
    for row in pCompAvg.index:
        for column in pCompAvg:
            if (column != 'player_name' and column != 'hand'): # will never iterate through first 2 columns because they are strings not floats
                # Input the percent different from average value for particular stat relative to the hand that the pitcher throws with
                # Note - this is done because metrics like xBreak and zBreak would cancel each other out since a right handed pitcher's pitch breaks a different direction than a left handed pitcher's pitch. Thus, the averages must be separated
                if (pCompAvg.at[row, 'hand'] == 'R'):
                    pCompAvg.at[row, column] = (pCompAvg.at[row, column] - RHPaverages.at[column, 0]) / RHPaverages.at[column, 0]
                else:
                    pCompAvg.at[row, column] = (pCompAvg.at[row, column] - LHPaverages.at[column, 0]) / LHPaverages.at[column, 0]
    return(pCompAvg)