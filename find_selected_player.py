{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "find_selected_player.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNAYSRjPFU0zMajTdU5sP2Z",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/find_selected_player.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BinHclpFmdro"
      },
      "outputs": [],
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
      ]
    }
  ]
}