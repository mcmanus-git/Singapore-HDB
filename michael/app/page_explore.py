# import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html, dcc
from navbar import create_navbar, create_footer
from app import app

nav = create_navbar()
discloser, footer = create_footer()




def create_page_explore():
    layout = html.Div([
        nav,
        html.Div([dcc.Markdown("Explore Page")], style={'margin': '5% 10% 5% 10%'}),
        discloser,
        footer

    ]
    )

    return layout

