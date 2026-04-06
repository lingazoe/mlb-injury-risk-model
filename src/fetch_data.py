import pybaseball as pb
import pandas as pd
from injury_list import clean_injury_list

TRAINING_YEAR = 2025
CURRENT_DT = '2026-04-05'
DIRECTORY = 'data/raw/'

def download_statcast():

    statcast_data = pb.statcast(start_dt='2025-03-28', end_dt=CURRENT_DT)
    statcast_data.to_csv(f'{DIRECTORY}statcast_data_25-26.csv', index=False)

def download_sprint_data():

    sprint_data = pb.statcast_sprint_speed(TRAINING_YEAR)
    sprint_data.to_csv(f'{DIRECTORY}sprint_data_2025.csv', index=False)

def download_metrics():

    bat_ev_data = pb.statcast_batter_exitvelo_barrels(TRAINING_YEAR)
    bat_ev_data.to_csv(f'{DIRECTORY}bat_ev_data_2025.csv', index=False)

    pitch_ev_data = pb.statcast_pitcher_exitvelo_barrels(TRAINING_YEAR)
    pitch_ev_data.to_csv(f'{DIRECTORY}pitch_ev_data_2025.csv', index=False)

def download_injury():

    injured_players_data = clean_injury_list("https://www.espn.com/mlb/injuries")   
    injured_players_data.to_csv(f'{DIRECTORY}injured_players_data_2026.csv')

def download_laham(): pb.download_lahman()

if __name__ == "__main__":

    download_statcast()
    download_sprint_data()
    download_metrics()
    download_injury()
    download_laham()


