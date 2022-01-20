{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "assign_difference_scores.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP18yEFRZTQNTnIB/9d9qvh",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/assign_difference_scores.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fiVdKUhUngM7"
      },
      "outputs": [],
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
      ]
    }
  ]
}