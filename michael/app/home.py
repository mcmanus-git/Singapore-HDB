# import dash_html_components as html
from dash import html
from dash import dcc
from navbar import create_navbar
import pandas as pd
from MyCreds.mycreds import Capstone_AWS_PG
from sqlalchemy import create_engine

test_query = 'select id from resale_prices_norm limit 1;'

engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_PG.username}:{Capstone_AWS_PG.password}@{Capstone_AWS_PG.host}/capstone', echo=False)

sql_alc_cnxn = engine.connect()
df = pd.read_sql(test_query, sql_alc_cnxn)


nav = create_navbar()

header_string = f'Welcome to home page!  {df.values[0]}'
header = html.H1(header_string)

markdown_text = dcc.Markdown("""
# Test Header  
Some placeholder text.  
```python
python = 'cool'
```  

""")


def create_page_home():
    layout = html.Div([
        nav,
        # Margin Top, Right, Bottom, Left
        html.Div([header], style={'margin': '20px 200px 10px 200px', 'flex': 1}),
        html.Div([markdown_text], style={'margin': '20px 200px 10px 200px', 'flex': 1})
    ])
    return layout
