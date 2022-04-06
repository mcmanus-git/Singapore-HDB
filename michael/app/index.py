# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from home import create_page_home
from page_blog import create_page_blog
from page_3 import create_page_3
from page_search_results import create_page_search_results
from app import app
import pandas as pd
import geopandas as gpd
from MyCreds.mycreds import MapBox
import plotly.express as px
import re

server = app.server
app.config.suppress_callback_exceptions = True

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
                                mapbox_style='carto-positron',
                                # symbol='park'
                                # # marker = {'size': 20, 'symbol': ["airport"]}
                                )


app.layout = dbc.Container(html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
]), fluid=True, className="dbc")


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/blog':
        return create_page_blog()
    if pathname == '/page-3':
        return create_page_3()
    if re.match('(/\d+)', pathname):
        return create_page_search_results(pathname)
    else:
        return create_page_home(sg_base_map)


if __name__ == '__main__':
    app.title = "WhyHigh"
    app.run_server(debug=True)
