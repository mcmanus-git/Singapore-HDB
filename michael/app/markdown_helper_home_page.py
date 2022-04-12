import geopandas as gpd
from sqlalchemy import create_engine
from MyCreds.mycreds import Capstone_AWS_SG
from datetime import datetime


def get_explore_column_data():
    sql = f"""SELECT * FROM resale_location_features where extract(year from month) >= {(datetime.now().year - 5)};"""

    engine = create_engine(
        f'postgresql+psycopg2://{Capstone_AWS_SG.username}:{Capstone_AWS_SG.password}@{Capstone_AWS_SG.host}/Capstone',
        echo=False)

    with engine.connect() as cnxn:
        df = gpd.read_postgis(sql, cnxn, geom_col='geometry')

    address_most_resales = df[df['address'] == df.value_counts('address').reset_index() \
        .rename({0: 'Number of Resales'}, axis=1).iloc[0]['address']][['address', 'building_id']].iloc[0].values
    address_highest_resale = df[df['resale_price_norm'] == df['resale_price_norm'].max()][
        ['address', 'building_id']].values
    address_lowest_resale = df[df['resale_price_norm'] == df['resale_price_norm'].min()][
        ['address', 'building_id']].values

    return address_highest_resale, address_lowest_resale, address_most_resales


def create_explore_column_markdown():
    highest, lowest, most = get_explore_column_data()

    explore_text = f"""## Highest Resale Price  
[{highest[0][0]}]({int(highest[0][1])})  
## Lowest Resale Price  
[{lowest[0][0]}]({int(lowest[0][1])})  
## Address Resold the Most Times  
[{most[0]}]({int(most[1])})  
  
  
*Data based on the last 5 years.*"""

    return explore_text
