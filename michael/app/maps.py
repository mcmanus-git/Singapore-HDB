import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
from MyCreds.mycreds import MapBox
from database_helpers import DatabaseHelpers

map_style_global = 'light'#'carto-positron'


def create_sg_base_map():
    sg_map_data = pd.DataFrame({0: {'latitude': 1.3521, 'longitude': 103.8198}}).T
    sg_map_data = gpd.GeoDataFrame(
        sg_map_data, geometry=gpd.points_from_xy(sg_map_data['longitude'], sg_map_data['latitude']))

    px.set_mapbox_access_token(MapBox.token)
    sg_base_map = px.scatter_mapbox(sg_map_data,
                                    lat=sg_map_data['geometry'].y,
                                    lon=sg_map_data['geometry'].x,
                                    center={'lat': 1.3521, 'lon': 103.8198},
                                    zoom=10,
                                    # width=500,
                                    height=600,
                                    opacity=0.1,
                                    mapbox_style=map_style_global,
                                    # symbol='park'
                                    # # marker = {'size': 20, 'symbol': ["airport"]}
                                    )
    return sg_base_map


def create_search_results_map(pathname):
    pathname = pathname.strip("/")

    address_geo_search = f"""SELECT *
FROM hdb_property_info a
LEFT JOIN sg_buildings_postal_geo b
ON CONCAT(a.blk_no,' ',a.street) = CONCAT(b.blk_no,' ',b.short_r_name)
where building_id = {pathname};"""

    engine = DatabaseHelpers.engine
    with engine.connect() as cnxn:
        df = gpd.read_postgis(address_geo_search, cnxn, geom_col="geometry")

    # print(df['geometry'].y[0])
    address_map = go.Figure(go.Scattermapbox(mode='markers+text',
                                             lon=[float(df['geometry'].x[0])],
                                             lat=[float(df['geometry'].y[0])],
                                             marker={'size': 20, 'symbol': ['star']},
                                             text=[*df['address_to_match'].values],
                                             textposition='bottom center'
                                             ))

    address_map.update_layout(mapbox=dict(accesstoken=MapBox.token,
                                          style=map_style_global,
                                          center=go.layout.mapbox.Center(lat=df['geometry'].y[0],
                                                                         lon=df['geometry'].x[0]),
                                          zoom=12
                                          ),
                              showlegend=False,
                              )

    # px.set_mapbox_access_token(MapBox.token)
    # address_map = px.scatter_mapbox(
    #     df,
    #     lat=df['geometry'].y,
    #     lon=df['geometry'].x,
    #     zoom=15,
    #     height=600,
    #     mapbox_style=map_style_global,
    #     symbol="fa fa-shield" # {'symbol': 'marker'}
    # )

    return address_map
