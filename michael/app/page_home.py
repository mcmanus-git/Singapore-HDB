# import dash_html_components as html
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
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
from markdown_helper_home_page import get_explore_column_data


# Note to self:
# Margin Top, Right, Bottom, Left

nav = create_navbar()

def create_page_home(sg_base_map):
    layout = html.Div([
        nav,

        # html.Div([header], style={'margin': '5% 10% 5% 10%', 'flex': 10, 'flex-direction': 'column',
        #                           'justify-content': 'left', 'text-align': 'center'}),
        html.Div([dcc.Graph(figure=sg_base_map)]),

        html.Div([
            dbc.Row([
                dbc.Col(html.Div([dcc.Markdown("""# Explore  
Unfamiliar with Singapore?  Explore one of the addresses below."""),
                                  html.Br(),
                                  dcc.Markdown(get_explore_column_data())
                                  ])),
                dbc.Col(
                    html.Div([
                        # html.P("Search Address"),
                        dcc.Input(id='address_search_input', type='text', placeholder='Enter Address', debounce=True, style=dict(
                            width='70%'
                        )),
                        dcc.Loading(
                            id="address_search_input_loading",
                            children=[html.Div([html.Br(),
                                                html.Div(id="address_search_output")])],
                            type="cube",
                            color='#4ABF72',
                            # fullscreen=True
                        ),

                    ])
                ),

            ])
        ],
            style={'margin': '0% 10% 5% 10%'}
        )

        #style={'margin': '20px 200px 10px 200px', 'flex': 1, 'flex-direction': 'column'})
        # dict(display='flex', justifyContent='center')) # Another way

    ])
    return layout

@app.callback(
    Output('address_search_output', 'children'),
    # Output('address_search_loading_output', 'children'),
    Input('address_search_input', 'value'),
    prevent_initial_call=True
)
def get_address_information(address_search_input):
    time.sleep(1)
    search_results = return_search_results(address_search_input)

    # return f"Address: {search_results}"
    return search_results