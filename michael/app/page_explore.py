# import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html, dcc
from navbar import create_navbar, create_footer
from app import app
from sqlalchemy import create_engine
from MyCreds.mycreds import Capstone_AWS_SG, MapBox
import geopandas as gpd
import plotly.express as px

nav = create_navbar()
discloser, footer = create_footer()


def get_animation_df():
    sql = """select mp.zone_id, mp."SUBZONE_N", mp.geometry,  avg(lf.resale_price) as avg_resale, min(lf.resale_price) as min_resale, max(lf.resale_price) as max_resale, count(distinct(transaction_id)) as count_resale, extract(year from lf.month) as transaction_year
from master_plan_2019_subzone_boundary as mp
         join resale_location_features as lf
              on ST_Contains(mp.geometry, lf.geometry)

group by transaction_year, mp.zone_id, mp."SUBZONE_N", mp.geometry;"""

    #where extract(year from lf.month) > 2010

    engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_SG.username}:{Capstone_AWS_SG.password}@{Capstone_AWS_SG.host}/Capstone', echo=False)

    with engine.connect() as cnxn:
        locs_in_plan = gpd.read_postgis(sql, cnxn, geom_col='geometry')

    return locs_in_plan


def create_animated_map(df):
    resale_locs_map_1990_Current = px.scatter_mapbox(df,
                                                     lat=df['geometry'].representative_point().y,
                                                     lon=df['geometry'].representative_point().x,
                                                     animation_frame=df["transaction_year"].astype(int),
                                                     hover_name="SUBZONE_N",
                                                     zoom=10,
                                                     color=df['avg_resale'],
                                                     size = df['count_resale'],
                                                     color_continuous_scale=px.colors.cyclical.IceFire,
                                                     size_max=15,
                                                     height=600,
                                                     opacity=0.7,
                                                     mapbox_style='light',
                                                     )
    return resale_locs_map_1990_Current


def create_page_explore():
    df = get_animation_df()
    animated_map = create_animated_map(df)
    layout = html.Div([
        nav,
        html.Div([dcc.Markdown("Explore Page")], style={'margin': '5% 10% 5% 10%'}),
        html.Div([dcc.Graph(figure=animated_map)]),
        discloser,
        footer

    ]
    )

    return layout

