{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "print_results.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOMuvHplEMVNpTWqRdUHoIV",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/print_results.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Odwis6RLnrQP"
      },
      "outputs": [],
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
      ]
    }
  ]
}