# import dash_html_components as html
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar
import pandas as pd
from MyCreds.mycreds import Capstone_AWS_PG
from sqlalchemy import create_engine
from app import app
from dash.dependencies import Input, Output
from address_search import return_search_results
import time

nav = create_navbar()

header_string = f'Welcome to home page!'
header = html.H1(header_string)

markdown_text = dcc.Markdown("""
# Test Header  
Please enter an address to search or select from the addresses to the left.
""")


def create_page_home():
    layout = html.Div([
        nav,
        # Margin Top, Right, Bottom, Left
        html.Div([header], style={'margin': '5% 10% 5% 10%', 'flex': 10, 'flex-direction': 'column',
                                  'justify-content': 'left', 'text-align': 'center'}),
        html.Div([markdown_text,
                  dbc.Button("Button", outline=True, color="danger", className="me-1")
                  ], style={'margin': '1% 10% 10% 10%', 'flex': 10}),
        html.Div([
            html.P("Search Address"),
            dcc.Input(id='address_search_input', type='text', placeholder='Enter Address', debounce=True, style=dict(
                width='30%',
                # display='table-cell',
            )),#{'marginRight':'10px'}),
            # html.Div(id='address_search_output'),
            dcc.Loading(
                id="address_search_input_loading",
                children=[html.Div(id="address_search_output")],
                type="cube",
                color='#4ABF72'
            ),
            # html.Div(id='address_search_output')

        ], style={'margin': '5% 10% 10% 10%'})
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

    return f"Address: {search_results}"
