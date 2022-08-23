# Pitcher-Comparison-Project
Author: Jack Lambert

## Project Overview
The goal of this project is to quantify a comparison between the raw characteristics (velocity, spin rate, spin axis, movement, and release point) of any two pitches with comparison scores. These comparison scores can not only be utilized to predict success, but also give insights into specific approaches that are proven to be effective with the raw characteristics a pitch has. 

Regarding the score itself, the smaller a score, the more similar two pitches are. The minimum score, 0, indicates two identical pitches (based on raw characteristics), and each score represents the average number of standard deviations two pitches differ by across all raw pitch characteristics considered. A full writeup of the project can be found here: [Comparison Scores Explained.pdf](https://github.com/jacklambert1/Pitcher-Comparison-Project/files/9382836/Comparison.Scores.Explained.pdf)

## Requirements
- All scripts executed using Python 3.10.6
  - Main.py compiles all data from https://baseballsavant.mlb.com/ and creates master.csv as well as scores.csv by calling the other scripts
  - Visualizations.ipynb contains exploratory analysis of master.csv and scores.csv and all visualizations found in [Comparison Scores Explained.pdf](https://github.com/jacklambert1/Pitcher-Comparison-Project/files/9382836/Comparison.Scores.Explained.pdf)
- Libraries used in Main.py:
  - urllib.request
  - re
  - os
  - pandas
  - numpy
  - sklearn
  - xgboost
- Libraries used in Visualizations.ipynb
  - pandas
  - matplotlib
  - numpy
  - colorama
  - sklearn
  - scipy

## How it Works
Execution of Main.py will trigger the sequence of events that compiles all of the comparison scores. Upon execution, the up-to-date velocity, spin, movement, release point, and pitch results data will be scraped from https://baseballsavant.mlb.com/. This data will be consolidated into the "master" CSV file with each row representing a distinct pitch. The "scores" CSV file will then be created, containing the comparison scores for all relevant pitches. Once these two CSV files are created, the user is able to explore master.csv and scores.csv for trends. Initial findings from these datasets are found here: [Comparison Scores Explained.pdf](https://github.com/jacklambert1/Pitcher-Comparison-Project/files/9382836/Comparison.Scores.Explained.pdf)
