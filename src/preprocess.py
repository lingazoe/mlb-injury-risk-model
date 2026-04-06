import pandas as pd
import pybaseball as pb

DIRECTORY_R = 'data/raw/'
DIRECTORY_P = 'data/processed/'

def player_lookup():

    register = pb.playerid_reverse_lookup(range(1, 1000000), key_type='mlbam')

    return register

def injured_to_ids():

    injury_data = pd.read_csv(f'{DIRECTORY_R}injured_players_data_2026.csv')

    register_path = f'{DIRECTORY_P}player_id_map.csv'

    register_content = pd.read_csv(register_path)

    def clean_name(name):
        return name.replace('.', '').replace('Jr', '').replace('Sr', '').strip().lower()
    
    injury_data['clean_name'] = injury_data['NAME'].apply(clean_name)
    register_content['clean_name'] = (register_content['name_first'] + ' ' + register_content['name_last']).apply(clean_name)

    injured_combined = pd.merge(
        injury_data, register_content[['clean_name', 'key_mlbam']], on='clean_name', how='left'
    )

    injured_combined.to_csv(f'{DIRECTORY_P}injured_players_2026.csv', index=False)

if __name__ == "__main__":
    injured_to_ids()