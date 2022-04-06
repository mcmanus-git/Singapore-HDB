# import dash_html_components as html
from dash import html
from navbar import create_navbar
from maps import create_search_results_map
from dash import dcc

nav = create_navbar()


def create_page_search_results(path):
    layout = html.Div([
        nav,
        html.Div([html.H3(f"User Chose: {path.strip('/')}")],
                 style={'margin': '5% 10% 10% 10%'}
                 ),
        html.Div([dcc.Graph(figure=create_search_results_map(path))]
                 )
    ])
    return layout
