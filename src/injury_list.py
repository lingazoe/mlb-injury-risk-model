import pandas as pd
from extraction import extract_data

def clean_injury_list(url):

    injury_data = pd.read_html(url)

    injury_data = pd.concat(injury_data, ignore_index=True)

    pd.set_option('display.max_columns', None)

    injury_data['INJURY_DATE'] = injury_data['COMMENT'].str.extract(r'^(\w{3} \d+)')
    injury_data['INJURY_DATE'] = pd.to_datetime(injury_data['INJURY_DATE'] + ', 2026')

    injury_data[['injured_body_part', 'injured_side', 'is_accidental']] = injury_data['COMMENT'].apply(lambda x: pd.Series(extract_data(x)))

    return injury_data
