{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "IMPROVED_Pitcher_Comparison_Project.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMNt+4hneZstq18Ps2g56wG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/IMPROVED_Pitcher_Comparison_Project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CE3bZNxTrUL9"
      },
      "outputs": [],
      "source": [
        "# Import necessary libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "# Read in data of MLB pitcher's statsitics from 2021 season\n",
        "pComps = pd.read_csv('https://raw.githubusercontent.com/jacklambert1/Pitcher-Comparison-Project/main/2021_pitcher_data.csv')\n",
        "pCompAvg = pComps.copy()\n",
        "\n",
        "# Initialize DataFrame with columns of every different pitch type monitored in 2021 season and rows of chosen comparison statistics\n",
        "# Since DataFrames contain indexing this DataFrame will be accessed relative to column name (for pitch type) and index value (for attribute for that pitch type)\n",
        "# Note - 'xx_comps' and 'xx_score' are not a part of the original data set, but will have values relative to individual pitch so are included in the creation of DataFrame\n",
        "fourseam = ['ff_speed', 'ff_spin', 'ff_xBreak', 'ff_zBreak', 'ff_RPx', 'ff_RPz', 'release_extension', 'ff_comps', 'ff_score']\n",
        "cutter = ['fc_speed', 'fc_spin', 'fc_xBreak', 'fc_zBreak', 'fc_RPx', 'fc_RPz', 'release_extension', 'fc_comps', 'fc_score']\n",
        "sinker = ['si_speed', 'si_spin', 'si_xBreak', 'si_zBreak', 'si_RPx', 'si_RPz', 'release_extension', 'si_comps', 'si_score']\n",
        "splitter = ['fs_speed', 'fs_spin', 'fs_xBreak', 'fs_zBreak', 'fs_RPx', 'fs_RPz', 'release_extension', 'fs_comps', 'fs_score']\n",
        "slider = ['sl_speed', 'sl_spin', 'sl_xBreak', 'sl_zBreak', 'sl_RPx', 'sl_RPz', 'release_extension', 'sl_comps', 'sl_score']\n",
        "curveball = ['cu_speed', 'cu_spin', 'cu_xBreak', 'cu_zBreak', 'cu_RPx', 'cu_RPz', 'release_extension', 'cu_comps', 'cu_score']\n",
        "changeup = ['ch_speed', 'ch_spin', 'ch_xBreak', 'ch_zBreak', 'ch_RPx', 'ch_RPz', 'release_extension', 'ch_comps', 'ch_score']\n",
        "pitchInfo = pd.DataFrame(list(zip(fourseam, cutter, sinker, splitter, slider, curveball, changeup)), \n",
        "                         columns = ['Four Seam Fastball', 'Cutter', 'Sinker', 'Splitter', 'Slider', 'Curveball', 'Changeup'])\n",
        "\n",
        "# Takes the average for each statistic of data set for all right handed pitchers and all left handed pitchers\n",
        "RHPaverages = find_averages(pComps, 'R')\n",
        "LHPaverages = find_averages(pComps, 'L')\n",
        "\n",
        "# Changes all values of original data set to the percent difference between original value and league average for each player's throwing hand\n",
        "pCompAvg = compare_vs_averages(pCompAvg, RHPaverages, LHPaverages)\n",
        "\n",
        "# Prompts the user to select a pitcher and continues to do so until they enter a valid pitcher name (when this is done, chosenPlayerLoc changes from -1 to whichever index value the valid player is in the pComps DataFrame)\n",
        "chosenPlayerLoc = -1\n",
        "while (chosenPlayerLoc == -1):\n",
        "    chosenPlayerLoc = find_selected_player(pComps, chosenPlayerLoc)\n",
        "\n",
        "# Creates new DataFrame full of data of the absolute value of the difference (in percent difference from average) for all pitchers that throw with same hand as selected pitcher\n",
        "eligiblePlayerComps = find_selected_player_comps(pCompAvg, chosenPlayerLoc)\n",
        "\n",
        "# Adds 'xx_comps' column in 'eligiblePlayerComps' DataFrame which represents number of comparisons possible between selected player and each other eligible player (same throwing hand)\n",
        "for column in pitchInfo:\n",
        "    eligiblePlayerComps[pitchInfo.at[7, column]] = np.nan\n",
        "\n",
        "# Fills in the 'xx_comps' column in 'eligiblePlayerComps' DataFrame with minimum of either 4 comparisons (every player has data on speed, spin, xBreak, and zBreak), 5 comparisons (some players are missing data on RPx and RPz), 6 comparisons (some players are missing data on release_extension), or 7 comparisons (all possible data is present)\n",
        "for row in eligiblePlayerComps.index:\n",
        "    eligiblePlayerComps = assign_comp_vals(eligiblePlayerComps, pitchInfo, row)\n",
        "\n",
        "# Initialize DataFrame to represent the Difference Scores of each player (Difference Score is calculated by the average difference between the percent difference from average there is between selected player and all other players in the data set for each stat)\n",
        "# Note - the lower the Difference Score the more similar the pitcher is\n",
        "nameData = eligiblePlayerComps['player_name'].to_list()\n",
        "ffScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "slScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "chScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "cuScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "siScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "fcScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "fsScoreData = [np.nan] * len(eligiblePlayerComps.index)\n",
        "differenceScores = pd.DataFrame(list(zip(nameData, ffScoreData, slScoreData, chScoreData, cuScoreData, siScoreData, fcScoreData, fsScoreData)), \n",
        "                                columns = ['player_name', 'ff_score', 'sl_score', 'ch_score', 'cu_score', 'si_score', 'fc_score', 'fs_score'])\n",
        "\n",
        "# Fills in the Difference Score for each player and each pitch\n",
        "difScoreRow = 0\n",
        "for row in eligiblePlayerComps.index:\n",
        "    differenceScores = assign_difference_scores(eligiblePlayerComps, differenceScores, pitchInfo, row, difScoreRow)\n",
        "    difScoreRow += 1\n",
        "\n",
        "# Prints the conclusions from the program: which player's are most similar to the selected player for each pitch in the selected player's repertoire\n",
        "# Note - the value that is printed is the Similarity Score (1 - Difference Score) not the Difference Score -- this is becuase it is  easier to think about the Similarity Score as 1 meaning the pitchers have the exact same metrics, rather than the Difference Score as 0 meaning they have no difference in their metrics\n",
        "nComps = 3 # nComps can change based on how many similar pitchers the user wants to see (ex: right now the top 3 for each pitch are displayed)\n",
        "print(pComps.at[chosenPlayerLoc, 'player_name'], 'Pitch Repertoire:')\n",
        "print_results(differenceScores, pComps, pitchInfo, chosenPlayerLoc, nComps)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def find_averages(pComps, hand):\n",
        "    data = []\n",
        "    for row in pComps.index:\n",
        "        if (pComps.at[row,'hand'] == hand): \n",
        "            data.append(pComps.loc[row]) # if player of current iteration throws with the chosen hand value then add that player's data to the list\n",
        "        \n",
        "    averages = pd.DataFrame(data)\n",
        "\n",
        "    # No need to take averages of strings so they can be deleted\n",
        "    del averages['player_name']\n",
        "    del averages['hand']\n",
        "\n",
        "    averages = pd.DataFrame(averages.mean()) # shortens the DataFrame from many rows to a single one of averages\n",
        "    return(averages)"
      ],
      "metadata": {
        "id": "w-nkLVWoFqm6"
      },
      "execution_count": 101,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def compare_vs_averages(pCompAvg, RHPaverages, LHPaverages):\n",
        "    for row in pCompAvg.index:\n",
        "        for column in pCompAvg:\n",
        "            if (column != 'player_name' and column != 'hand'): # will never iterate through first 2 columns because they are strings not floats\n",
        "                # Input the percent different from average value for particular stat relative to the hand that the pitcher throws with\n",
        "                # Note - this is done because metrics like xBreak and zBreak would cancel each other out since a right handed pitcher's pitch breaks a different direction than a left handed pitcher's pitch. Thus, the averages must be separated\n",
        "                if (pCompAvg.at[row, 'hand'] == 'R'):\n",
        "                    pCompAvg.at[row, column] = (pCompAvg.at[row, column] - RHPaverages.at[column, 0]) / RHPaverages.at[column, 0]\n",
        "                else:\n",
        "                    pCompAvg.at[row, column] = (pCompAvg.at[row, column] - LHPaverages.at[column, 0]) / LHPaverages.at[column, 0]\n",
        "    return(pCompAvg)"
      ],
      "metadata": {
        "id": "vyG0_ThZHxsg"
      },
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def find_selected_player(pComps, chosenPlayerLoc):\n",
        "    userPlayer = input('Enter an MLB pitcher''s name in the \"Lastname, Firstname\" format: ') # asks user to input player name in format consistent with pComps DataFrame\n",
        "    # Iterate through all rows of pComps looking for the player the user named\n",
        "    for row in pComps.index:\n",
        "        if (pComps.at[row, 'player_name'] == userPlayer):\n",
        "            chosenPlayerLoc = row # chosenPlayerLoc will be used to reference the chosen player now throughout the program\n",
        "            break # if the player is found there is no reason to finish iterating through the loop so exit\n",
        "    # If the player was not found in the whole pComps DataFrame (this is known by chosenPlayerLoc not changing from its original value of -1) then tell user the input was invalid\n",
        "    if (chosenPlayerLoc == -1):\n",
        "        print('Invalid entry.')\n",
        "    return(chosenPlayerLoc)"
      ],
      "metadata": {
        "id": "4Vo5nSxSIcxe"
      },
      "execution_count": 99,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def find_selected_player_comps(pCompAvg, chosenPlayerLoc):\n",
        "    eligiblePlayerCompsList = []\n",
        "    # For all data points in pCompAvg, copy them over to a list (eventually to be turned into a DataFrame) if the player of current iteration throws with the same hand as the selected player but is not the selected player\n",
        "    # Note - the selected player would have a Similarity Score of 1 (identical) so there is no point in including them\n",
        "    for row in pCompAvg.index:\n",
        "        if ((pCompAvg.at[row,'hand'] == pCompAvg.at[chosenPlayerLoc,'hand']) and (pCompAvg.at[row, 'player_name'] != pCompAvg.at[chosenPlayerLoc, 'player_name'])):\n",
        "            eligiblePlayerCompsList.append(pCompAvg.loc[row])\n",
        "    eligiblePlayerComps = pd.DataFrame(eligiblePlayerCompsList)\n",
        "    # For all eligible players, change each metric's value to the absolute value of the difference between the selected player's difference from average metric and the current iteration player's difference from average metric\n",
        "    for row in eligiblePlayerComps.index:\n",
        "        eligiblePlayerComps.loc[row,'ff_speed':'fs_RPz'] = abs(pCompAvg.loc[chosenPlayerLoc, 'ff_speed':'fs_RPz'] - eligiblePlayerComps.loc[row, 'ff_speed':'fs_RPz'])\n",
        "    return(eligiblePlayerComps)"
      ],
      "metadata": {
        "id": "Nw-eO-oKRQmv"
      },
      "execution_count": 98,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def assign_comp_vals(eligiblePlayerComps, pitchInfo, row):\n",
        "    # Iterating through all columns of 'pitchInfo' allows for all values for each specific pitch to be referenced and changed\n",
        "    # Note - each pitch type is represented by column name and each attribute of pitch type is represented by index value\n",
        "    # Note - in this function the values 0 (xx_speed), 4 (xx_RPx), 5 (xx_RPz), 6 (release_point), and 7 (xx_comps) are referenced\n",
        "    for column in pitchInfo:\n",
        "        if (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[0, column]]) == False): # only assign a comp value if the current iteration's pitcher throws that pitch (shown by the speed of that pitch being a numeric value)\n",
        "                if ((np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[4, column]]) == False) and (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[5, column]]) == False) and (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) == False)):\n",
        "                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 7\n",
        "                elif ((np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[4, column]]) == False) and (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[5, column]]) == False)):\n",
        "                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 6\n",
        "                elif (np.isnan(eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) == False):\n",
        "                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 5\n",
        "                else:\n",
        "                    eligiblePlayerComps.at[row, pitchInfo.at[7, column]] = 4\n",
        "    return(eligiblePlayerComps)"
      ],
      "metadata": {
        "id": "kT0KMB_m33kN"
      },
      "execution_count": 97,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def assign_difference_scores(eligiblePlayerComps, diffrenceScores, pitchInfo, row, difScoreRow):\n",
        "    # Iterating through all columns of 'pitchInfo' allows for all values for each specific pitch to be referenced and changed\n",
        "    # Note - each pitch type is represented by column name and each attribute of pitch type is represented by index value\n",
        "    # Note - in this function the values 0 (xx_speed), 1 (xx_spin), 2 (xx_xBreak), 3 (xx_zBreak), 4 (xx_RPx), 5 (xx_RPz), 6 (release_point), 7 (xx_comps), and 8 (xx_score) are referenced\n",
        "    for column in pitchInfo:\n",
        "        # Difference Score is an average of the absolute value of the difference between the selected player and all other players for all stats. Since not every player has data on 'xx_RPx', 'xx_RPz', and/or 'release_extension', the average is dependent on the number of comparisons they have\n",
        "        if (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 7):\n",
        "            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]] + eligiblePlayerComps.at[row, pitchInfo.at[4, column]] + eligiblePlayerComps.at[row, pitchInfo.at[5, column]] + eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]\n",
        "        elif (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 6):\n",
        "            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]] + eligiblePlayerComps.at[row, pitchInfo.at[4, column]] + eligiblePlayerComps.at[row, pitchInfo.at[5, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]\n",
        "        elif (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 5):\n",
        "            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]] + eligiblePlayerComps.at[row, pitchInfo.at[6, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]\n",
        "        elif (eligiblePlayerComps.at[row, pitchInfo.at[7, column]] == 4):\n",
        "            differenceScores.at[difScoreRow, pitchInfo.at[8, column]] = (eligiblePlayerComps.at[row, pitchInfo.at[0, column]] + eligiblePlayerComps.at[row, pitchInfo.at[1, column]] + eligiblePlayerComps.at[row, pitchInfo.at[2, column]] + eligiblePlayerComps.at[row, pitchInfo.at[3, column]]) / eligiblePlayerComps.at[row, pitchInfo.at[7, column]]\n",
        "    return(differenceScores)"
      ],
      "metadata": {
        "id": "t9pJfs6E-zGy"
      },
      "execution_count": 96,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def print_results(differenceScores, pComps, pitchInfo, chosenPlayerLoc, nComps):\n",
        "    # Iterating through all columns of 'pitchInfo' allows for all values for each specific pitch to be referenced and changed\n",
        "    # Note - each pitch type is represented by column name and each attribute of pitch type is represented by index value\n",
        "    # Note - in this function the values 0 (xx_speed) and 8 (xx_score) are referenced\n",
        "    for column in pitchInfo:\n",
        "        if (np.isnan(pComps.at[chosenPlayerLoc, pitchInfo.at[0, column]]) == False): # only print a pitch name and similar pitchers if the selected pitcher throws that pitch (shown by the speed of that pitch being a numeric value)\n",
        "            print(column)\n",
        "            print('   Most similar pitches:')\n",
        "            differenceScores.sort_values(pitchInfo.at[8, column], inplace = True) # Sorts values in 'differenceScores' from most similar to least similar for current pitch iteration\n",
        "            differenceScores.reset_index(drop = True, inplace = True)\n",
        "            for i in range(nComps):\n",
        "                print('    ', differenceScores.at[i, 'player_name'], '-- Similarity Score:', round(1 - differenceScores.at[i, pitchInfo.at[8, column]], 3)) # 1 - Difference Score = Similarity Score"
      ],
      "metadata": {
        "id": "xs4H2L7CCTv_"
      },
      "execution_count": 95,
      "outputs": []
    }
  ]
}