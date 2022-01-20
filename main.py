{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "main.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOmvy7DVsGhNt9ZkBqJCxbr",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "id": "MmPpzGDAn9as",
        "outputId": "16c70350-a001-4ce7-ef4f-bcc7d14d45cf"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-ad71df6c6315>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# Takes the average for each statistic of data set for all right handed pitchers and all left handed pitchers\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mRHPaverages\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfind_averages\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpComps\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'R'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0mLHPaverages\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfind_averages\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpComps\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'L'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'find_averages' is not defined"
          ]
        }
      ],
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
    }
  ]
}