{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "find_averages.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNCQcVhZTPrJ3jcT17RBQvE",
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
        "<a href=\"https://colab.research.google.com/github/jacklambert1/Pitcher-Comparison-Project/blob/main/find_averages.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9FwZ5jUhmCVe"
      },
      "outputs": [],
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
      ]
    }
  ]
}