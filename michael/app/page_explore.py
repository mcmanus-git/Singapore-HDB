# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar

nav = create_navbar()

def create_page_explore():
    layout = html.Div([
        nav,
        html.Div([dcc.Markdown("Explore Page")], style={'margin': '5% 10% 5% 10%'}),
    ])
    return layout
