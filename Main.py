import os

def run_scrapes():
    os.system("python3 Pitch_Characteristics_Scrape.py")
    os.system("python3 Axis_Scrape.py")
    os.system("python3 Run_Value_Scrape.py")

    print("All scrapes complete.")

def compile_data():
    os.system("python3 Compile_Data.py")

    print("Scraped data consolidated to one player data CSV.")

def scores():
    os.system("python3 Comparison_Scores.py")

    print("Comparison scores completed.")

def prep():
    os.system("python3 Final_Prep.py")

    print("Final updates to player data completed.")

# Run the initial data scraping scripts
run_scrapes()

# Run the script that combines the scrapes into workable data
compile_data()

# Run the script that makes the comparison scores file
scores()

# Run the script that polishes final data
prep()