# Pitcher-Comparison-Project

## Project Overview
The goal of this project is to quantify a comparison between the "stuff" of any two pitches. This "stuff" refers to the raw characteristics of a pitch: velocity, spin rate, spin angle, movement, and release point. In depth writeup on project found here: [Comparison Scores Explained.pdf](https://github.com/jacklambert1/Pitcher-Comparison-Project/files/9382836/Comparison.Scores.Explained.pdf)

## Script Overview
- Main.py
  - Once all scripts are downloaded, running Main.py will execute all of the scripts (other than Visualizations.ipynb) in the sequence they are meant to be executed in, scraping all data, compiling it into one CSV, creating comparison scores, and finalizing the master CSV
- Scrape Scripts
  - Pitch_Characteristics_Scrape.py
    - scrapes all velocity, spin rate, movement, and release point data from https://baseballsavant.mlb.com/
    - generates pitch_characteristics.csv
  - Axis_Scrape.py
    - scrapes all spin axis data from https://baseballsavant.mlb.com/
    - generates axis.csv
  - Run_Values.py
    - scrapes all Run Value per 100 data from https://baseballsavant.mlb.com/
    - generates run_values.csv
 - Compile_Data.py
    - compiles all scraped data into a single CSV, with each row representing an individual pitch
    - generates master.csv
 - Comparison_Scores.py
    - creates multipliers for comparison and then comparisons for all relevant scores
    - generates scores.csv
 - Final_Prep.py
    - updates master.csv with uniqueness categorization values
    - returns updated master.csv
 - Visualizations.ipynb
    - creates all visuals and features other exploratory analysis used in [Comparison Scores Explained.pdf](https://github.com/jacklambert1/Pitcher-Comparison-Project/files/9382836/Comparison.Scores.Explained.pdf)

## Requirements
- All scripts executed using Python 3.10.6
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
