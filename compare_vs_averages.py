{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "compare_vs_averages.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMiJbC1bgbkp8kAVep7mj1i",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/compare_vs_averages.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "loFsNa2ImUXv"
      },
      "outputs": [],
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
      ]
    }
  ]
}