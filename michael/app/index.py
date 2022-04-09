from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from page_home import create_page_home
from page_blog import create_page_blog
from page_contact_us import create_page_contact_us
from page_search_results import create_page_search_results
from app import app
import pandas as pd
import geopandas as gpd
from MyCreds.mycreds import MapBox
import plotly.express as px
import re
from maps import create_sg_base_map

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = dbc.Container(html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
]), fluid=True, className="dbc")


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/blog':
        return create_page_blog()
    if pathname == '/contact-us':
        return create_page_contact_us()
    if re.match(r'^(/\d+)', pathname):
        return create_page_search_results(pathname)
    else:
        sg_base_map = create_sg_base_map()
        return create_page_home(sg_base_map)


if __name__ == '__main__':
    app.title = "WhyHigh"
    app.run_server(debug=True)
