# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar, create_footer
from markdown_helper_explore_page import create_explore_column_markdown
from sqlalchemy import create_engine
from michael.app.MyCreds.mycreds import Capstone_AWS_SG
import geopandas as gpd
import plotly.express as px

nav = create_navbar()
discloser, footer = create_footer()


def get_animation_df():
    sql = """select * from resale_subzone_boundary;"""

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
                                                     size=df['count_resale'],
                                                     color_continuous_scale=px.colors.cyclical.IceFire,
                                                     size_max=25,
                                                     range_color=[200000, 1200000],
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
        html.Div([dcc.Markdown("### Explore Singapore")], style={'margin': '5% 10% 5% 10%'}),
        html.Div([dcc.Markdown("""Normalized HDB Resale Price over Year  
        Circle Color: Average Price In Planning Zone over Period | Circle Size: Number of Transactions in Period""")],
                 style={'margin': '1% 10% 0% 10%', 'font-size': '12px'}),
        html.Div([dcc.Graph(figure=animated_map)]),

        html.Div([dcc.Markdown("""## Historical Stats  """),
                  html.Br(),
                  dcc.Markdown(create_explore_column_markdown(),
                               style={"white-space": "pre"},
                               dangerously_allow_html=True)
                  ], style={'margin': '5% 10% 5% 10%'}),
        discloser,
        footer

    ]
    )

    return layout

