import pandas as pd
import numpy as np

def find_selected_player(pComps, chosenPlayerLoc):
    userPlayer = input('Enter an MLB pitcher''s name in the "Lastname, Firstname" format: ') # asks user to input player name in format consistent with pComps DataFrame
    # Iterate through all rows of pComps looking for the player the user named
    for row in pComps.index:
        if (pComps.at[row, 'player_name'] == userPlayer):
            chosenPlayerLoc = row # chosenPlayerLoc will be used to reference the chosen player now throughout the program
            break # if the player is found there is no reason to finish iterating through the loop so exit
    # If the player was not found in the whole pComps DataFrame (this is known by chosenPlayerLoc not changing from its original value of -1) then tell user the input was invalid
    if (chosenPlayerLoc == -1):
        print('Invalid entry.')
    return(chosenPlayerLoc)