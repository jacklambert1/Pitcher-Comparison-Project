def find_averages(pComps, hand):
    data = []
    for row in pComps.index:
        if (pComps.at[row,'hand'] == hand): 
            data.append(pComps.loc[row]) # if player of current iteration throws with the chosen hand value then add that player's data to the list
        
    averages = pd.DataFrame(data)

    # No need to take averages of strings so they can be deleted
    del averages['player_name']
    del averages['hand']

    averages = pd.DataFrame(averages.mean()) # shortens the DataFrame from many rows to a single one of averages
    return(averages)