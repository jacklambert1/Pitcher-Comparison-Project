{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "find_selected_player_comps.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPLOJHSBBSafC9p9V1mvUL8",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/find_selected_player_comps.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QUOM2rxzm5px"
      },
      "outputs": [],
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
      ]
    }
  ]
}