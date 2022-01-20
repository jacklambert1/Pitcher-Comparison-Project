{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "assign_comp_vals.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPCCZQlzeHxbmjdgGoafXoX",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/assign_comp_vals.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "km1IsT_znSHA"
      },
      "outputs": [],
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
      ]
    }
  ]
}