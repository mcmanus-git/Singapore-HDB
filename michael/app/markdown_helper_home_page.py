import geopandas as gpd
from sqlalchemy import create_engine
from MyCreds.mycreds import Capstone_AWS_SG
import pandas as pd


def get_explore_column_data():
    sql = f"""SELECT * FROM explore_pg_five_yr_min_max;"""

    engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_SG.username}:{Capstone_AWS_SG.password}@{Capstone_AWS_SG.host}/Capstone', echo=False)

    with engine.connect() as cnxn:
        df = pd.read_sql(sql, cnxn)

    df['aggregated_amount'] = df['aggregated_amount'].round(2)

    return df


def create_explore_column_markdown():
    df = get_explore_column_data()

    explore_text = f"""#### Highest Resale Price: 
${df[df['attribute'] == 'highest_resale'].iloc[0, 2]:,.2f}  
[{df[df['attribute'] == 'highest_resale'].iloc[0, 0]}]({int(df[df['attribute'] == 'highest_resale'].iloc[0, 1])})  

<br>

#### Lowest Resale Price  
${df[df['attribute'] == 'lowest_resale'].iloc[0, 2]:,.2f}  
[{df[df['attribute'] == 'lowest_resale'].iloc[0, 0]}]({int(df[df['attribute'] == 'lowest_resale'].iloc[0, 1])})  

<br>

#### Address with the Most Resold Flats:  
Resold {int(df[df['attribute'] == 'max_n_resales'].iloc[0, 2])} times.
[{df[df['attribute'] == 'max_n_resales'].iloc[0, 0]}]({int(df[df['attribute'] == 'max_n_resales'].iloc[0, 1])})  

<br>

*Data based on the last 5 years.*"""

    return explore_text
