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

test_query = 'select id from resale_prices_norm limit 1;'

engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_PG.username}:{Capstone_AWS_PG.password}@{Capstone_AWS_PG.host}/capstone', echo=False)

sql_alc_cnxn = engine.connect()
df = pd.read_sql(test_query, sql_alc_cnxn)


nav = create_navbar()

header_string = f'Welcome to home page!  {df.values[0]}'
header = html.H1(header_string)

markdown_text = dcc.Markdown("""
# Test Header  
Some placeholder text.  *Wow!* Green navbar.  Ok, that's pretty cool.  

    >
    > Block quotes are used to highlight text.
    >

e=mc^2  

```python
def get_something():
    python = 'cool'
    return python
```  



""")


def create_page_home():
    layout = html.Div([
        nav,
        # Margin Top, Right, Bottom, Left
        html.Div([header], style={'margin': '20px 200px 10px 200px', 'flex': 1}),
        html.Div([markdown_text,
                  dbc.Button("Button", outline=True, color="danger", className="me-1")
                  ], style={'margin': '20px 200px 10px 200px', 'flex': 1}),
        html.Div([
            html.I("Search Address"),
            html.Br(),
            dcc.Input(id='address_search_input', type='text', placeholder='Enter Address', debounce=True, style={'marginRight':'10px'}),
            # html.Div(id='address_search_output'),
            dcc.Loading(
                id="address_search_input_loading",
                children=[html.Div(id="address_search_output")],
                type="cube",
                color='#4ABF72'
            ),
            # html.Div(id='address_search_output')

        ], style={'margin': '20px 200px 10px 200px', 'flex': 1})

    ])
    return layout

@app.callback(
    Output('address_search_output', 'children'),
    # Output('address_search_loading_output', 'children'),
    Input('address_search_input', 'value')
)
def get_address_information(address_search_input):
    time.sleep(1)
    search_results = return_search_results(address_search_input)

    return f"Address: {search_results}"
