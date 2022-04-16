# import dash_html_components as html
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from navbar import create_navbar
import pandas as pd
from MyCreds.mycreds import Capstone_AWS_PG, MapBox
from sqlalchemy import create_engine
from app import app
from dash.dependencies import Input, Output
from address_search import return_search_results
import time
import plotly.express as px
import geopandas as gpd
from markdown_helper_home_page import create_explore_column_markdown
from page_search_results import create_page_search_results
from geopy.geocoders import Nominatim

# Note to self:
# Margin Top, Right, Bottom, Left
# 4459 33 TELOK BLANGAH WAY

nav = create_navbar()


def create_page_home(sg_base_map):
    layout = html.Div([
        nav,
        html.Div([dcc.Graph(figure=sg_base_map)]),

        html.Div([
            html.Div([
                dcc.Input(id='address_search_input', type='text', placeholder='Enter Address', debounce=False, style=dict(width='300px'))
            ], style={'display': 'inline-block', 'margin': '0% 0% 0% 0%'}
            ),
            html.Div([
                dcc.Dropdown(['1 Room', '2 Room', '3 Room', '4 Room', '5 Room', 'Multi Generation', 'Executive'], placeholder='Rooms', id='flat_type_search_input'),
            ], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin': '0% 1% 0% 1%', 'width': '20%'}
            ),
            html.Div([
                dcc.Dropdown([i for i in range(1, 52)], placeholder='Floor',  id='floor_search_input'),
            ], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin': '0% 1% 0% 1%', 'width': '10%'}
            ),
            html.Div([
                dcc.Input(id='sq_m_search_input', type='text', placeholder='Square Meters', debounce=True)
            ], style={'display': 'inline-block', 'margin': '0% 1% 0% 1%'}
            ),
            html.Div([
                dbc.Button(id='submit_address_search', n_clicks=0, children='Submit', color='success',
                           style={'display': 'inline-block'})#, href=f"/search-results")
            ], style={'display': 'inline-block', 'margin': '0% 0% 0% 1%'}
            ),
            html.Br(),
            html.Br(),
            html.Div(id='address_search_output'),
            html.Br(),
            html.Br(),
            html.Div([dcc.Markdown("""# Explore  
Unfamiliar with Singapore?  Explore one of the addresses below."""),
                      html.Br(),
                      dcc.Markdown(create_explore_column_markdown(),
                                   style={"white-space": "pre"},
                                   dangerously_allow_html=True)
                      ]),
        ],
            style={'margin': '0% 10% 5% 10%'})
    ])
    return layout


@app.callback(
    Output('address_search_output', 'children'),
    Input('submit_address_search', 'n_clicks'),
    State('address_search_input', 'value'),
    State('flat_type_search_input', 'value'),
    State('floor_search_input', 'value'),
    State('sq_m_search_input', 'value'),
    prevent_initial_call=True
)
def get_address_information(n_clicks, address, flat_type, floor, sq_m):
    time.sleep(1)
    # search_results = return_search_results(address, flat_type, floor, sq_m)
    search_results = f"{address}"
    # return f"Address: {search_results}"
    # return search_results
    # layout = create_page_search_results(n_clicks, address, flat_type, floor, sq_m)
    geolocator = Nominatim(user_agent="http://127.0.0.1:8050/")
    location = geolocator.geocode(address, namedetails=True)

    def sneaky_backdoor_test(n_clicks, address, flat_type, floor, sq_m):
        return n_clicks, address, flat_type, floor, sq_m

    # search_results = f"Address: {address}  Flat Type: {flat_type}"
    # search_results = dcc.Markdown(f"""Search Results:  [{location.address}](/search-results?{location.address.replace(' ', '-')}%{location.longitude}%{location.latitude}%{flat_type.replace(' ', '-')}%{floor}%{sq_m})""")
    search_results = dcc.Markdown(f"""Search Results   \n[{location.address}](/search-results?%{location.longitude}%{location.latitude}%{flat_type.replace(' ', '-')}%{sq_m})
    """)

    return search_results
