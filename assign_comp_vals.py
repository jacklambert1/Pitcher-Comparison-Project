def assign_comp_vals(eligiblePlayerComps, pitchInfo, row):
    # Iterating through all columns of 'pitchInfo' allows for all values for each specific pitch to be referenced and changed
    # Note - each pitch type is represented by column name and each attribute of pitch type is represented by index value
    # Note - in this function the values 0 (xx_speed), 4 (xx_RPx), 5 (xx_RPz), 6 (release_point), and 7 (xx_comps) are referenced
    for column in pitchInfo:
        if (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[0, column]]) == False): # only assign a comp value if the current iteration's pitcher throws that pitch (shown by the speed of that pitch being a numeric value)
                if ((np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[4, column]]) == False) and (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[5, column]]) == False) and (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) == False)):
                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 7
                elif ((np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[4, column]]) == False) and (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[5, column]]) == False)):
                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 6
                elif (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) == False):
                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 5
                else:
                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 4
    return(eligiblePlayerComps)