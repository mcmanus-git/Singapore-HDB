import geopandas as gpd
import numpy as np
import pandas as pd
import pickle
from database_helpers import DatabaseHelpers
from MyCreds.mycreds import Capstone_AWS_SG, MapBox
from collections import defaultdict, Counter
import re
from dash import dcc
from dash import html
from database_helpers import DatabaseHelpers
from MyCreds.mycreds import Capstone_AWS_SG
from geopy.geocoders import Nominatim


# def get_hdb_property_info():
#
#     sql = """SELECT a.blk_no, a.street, b.blk_no, b.short_r_name, b.postal, b.building_id
#     FROM hdb_property_info a
#     LEFT JOIN sg_buildings_postal_geo b
#     ON CONCAT(a.blk_no,' ',a.street) = CONCAT(b.blk_no,' ',b.short_r_name);"""
#
#     engine = DatabaseHelpers.engine
#
#     with engine.connect() as cnxn:
#         df = pd.read_sql(sql, cnxn)
#
#     df.columns = ['block_number', 'street', 'blk_no', 'short_r_name', 'postal', 'building_id']
#     df = df[['building_id', 'block_number', 'street', 'postal']]
#
#     return df
#
#
# def create_address_inv_indx():
#
#     with open('address_inverted_index.pkl', 'rb') as p:
#         address_inv_index = pickle.load(p)
#
#     return address_inv_index
#
#
# def get_search_results(search, n_results, address_inv_indx, hdb):
#
#     address_links = ""
#     address_no_results_message = "Sorry we weren't able to find the address you were looking for.  " \
#                                  "Please check the address and try again."
#
#     intersects = list(set.intersection(*map(set, [address_inv_indx[word.upper()] for word in search.split()])))
#     if len(intersects) > 0:
#         address_ids = intersects
#
#     else:
#         search_vals = defaultdict(list)
#
#         for word in search.split():
#             search_vals[word].append(address_inv_indx[word.upper()])
#
#         most_probable_addresses = Counter([item for sublist in search_vals.values() for lst in sublist for item in lst]).most_common()[:n_results]
#         address_ids = [most_probable_addresses[i][0] for i, _ in enumerate(most_probable_addresses)]
#
#     addresses = hdb[hdb['building_id'].isin(address_ids)].drop_duplicates()
#     addresses = addresses[~addresses.duplicated(subset=['block_number', 'street', 'postal'], keep='last')].values
#
#     for i, a in enumerate(addresses):
#         address_links += f"[{' '.join(a[1:])}]({int(a[0])})  \n"
#
#     search_results = html.Div(dcc.Markdown(f"""Search Results:
#     {address_links}
#
#
#     """))
#
#     return search_results


def address_search_query():

    sql = f"""select {", ".join(DatabaseHelpers.features)},
st_setsrid(st_makepoint(103.82243971608177, 1.2741913500000002), 4326)::geography <-> geometry::geography as distance
from resale_location_features
order by distance asc, month desc
limit 1;"""


    return sql

def get_search_results(search, flat_type, floor, sq_m):

    geolocator = Nominatim(user_agent=Capstone_AWS_SG.geo_user_agent)
    search = geolocator.geocode(search)
    # address_links =

    search_results = html.Div(dcc.Markdown(f"""Search Results:  
    


    """))

    return search_results


def return_search_results(search, flat_type, floor, sq_m):
    # n_results = 3
    # hdb = get_hdb_property_info()
    # add_inv_idx = create_address_inv_indx()
    search_results = get_search_results(search, flat_type, floor, sq_m)
    return search_results


if __name__ == '__main__':
    return_search_results()

