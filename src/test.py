import pandas as pd

url = "https://www.espn.com/mlb/injuries"
injury_data = pd.read_html(url)

injury_data = pd.concat(injury_data, ignore_index=True)

pd.set_option('display.max_columns', None)

injury_data['INJURY_DATE'] = injury_data['COMMENT'].str.extract(r'^(\w{3} \d+)')
injury_data['INJURY_DATE'] = pd.to_datetime(injury_data['INJURY_DATE'] + ', 2026')

print(injury_data.head())