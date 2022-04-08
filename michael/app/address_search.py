import geopandas as gpd
import numpy as np
import pandas as pd
import pickle
from sqlalchemy import create_engine
from MyCreds.mycreds import Capstone_AWS_PG, MapBox
from collections import defaultdict, Counter
import re
from dash import dcc
from dash import html
from database_helpers import DatabaseHelpers


def get_hdb_property_info():
    hdb_geo_query = """SELECT *
    FROM hdb_property_info a
    LEFT JOIN sg_buildings_postal_geo b
    ON CONCAT(a.blk_no,' ',a.street) = CONCAT(b.blk_no,' ',b.short_r_name)"""

    # engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_PG.username}:{Capstone_AWS_PG.password}@{Capstone_AWS_PG.host}/capstone', echo=False)
    engine = DatabaseHelpers.engine

    with engine.connect() as cnxn:
        df = gpd.read_postgis(hdb_geo_query, cnxn, geom_col='geometry')

    df.columns = ['block_number', 'street', 'max_floor_lvl', 'year_completed', 'residential',
                  'commercial', 'market_hawker', 'miscellaneous', 'multistorey_carpark',
                  'precinct_pavilion', 'bldg_contract_town', 'total_dwelling_units',
                  '1room_sold', '2room_sold', '3room_sold', '4room_sold', '5room_sold',
                  'exec_sold', 'multigen_sold', 'studio_apartment_sold', '1room_rental',
                  '2room_rental', '3room_rental', 'other_room_rental', 'building_id',
                  'address', 'blk_no', 'building', 'latitude', 'longitude', 'longtitude',
                  'postal', 'road_name', 'short_r_name', 'searchval', 'x', 'y',
                  'address_to_match', 'geometry']

    df.dropna(inplace=True)

    return df


def create_address_inv_indx():
    # address_inv_index = defaultdict(list)
    # for i, address in enumerate((df['block_number'] + " " + df['street'] + " " + df['postal'])):
    #     address = " ".join(*re.findall('(^\d+)(...+)', address)).replace('  ', ' ')
    #     for word in address.split():
    #         address_inv_index[word].append(int(df.iloc[i]['building_id']))

    with open('address_inverted_index.pkl', 'rb') as p:
        address_inv_index = pickle.load(p)

    return address_inv_index


def get_search_results(search, n_results, address_inv_indx, hdb):

    search_vals = defaultdict(list)

    search = " ".join(*re.findall('(^\d+)(...+)', search)).replace('  ', ' ')

    for word in search.split():
        search_vals[word].append(address_inv_indx[word.upper()])

    # __________________________________________________________________________________________________________
    # Using Frequency KEEP
    # most_probable_addresses = Counter([item for sublist in search_vals.values() for lst in sublist for item in lst]).most_common()[:n_results]
    #
    # address_ids = [most_probable_addresses[i][0] for i, _ in enumerate(most_probable_addresses)]
    # __________________________________________________________________________________________________________


    # Example of Using Intersection to Find Probable Address IDs
    # most_probable_addresses = list(set.intersection(*map(set, [address_inv_indx['33'],
    #                                                            address_inv_indx['TELOK'],
    #                                                            address_inv_indx['BLANGAH'],
    #                                                            address_inv_indx['WAY']
    #                                                            ]
    #                                                      )))

    address_ids = list(set.intersection(*map(set, [address_inv_indx[word.upper()] for word in search.split()])))




    addresses = pd.DataFrame()
    for id in address_ids:
        addresses = pd.concat([addresses, hdb[hdb['building_id'] == id]])

    addresses = addresses[['building_id', 'block_number', 'street', 'postal']].drop_duplicates().values
    print(addresses, type(addresses))

    address_links = ""
    for i, a in enumerate(addresses):
        address_links += f"[{' '.join(a[1:])}]({int(a[0])})  \n"




    # [{" ".join(addresses[0][1:])}]({int(addresses[0][0])})
    # [{" ".join(addresses[1][1:])}]({int(addresses[1][0])})
    # [{" ".join(addresses[2][1:])}]({int(addresses[2][0])})

    search_results = html.Div(dcc.Markdown(f"""Search Results:  
    {address_links}
    
    
    """))

    return search_results


def return_search_results(search):
    n_results = 3
    hdb = get_hdb_property_info()
    add_inv_idx = create_address_inv_indx()
    search_results = get_search_results(search, n_results, add_inv_idx, hdb)
    return search_results


if __name__ == '__main__':
    return_search_results()
