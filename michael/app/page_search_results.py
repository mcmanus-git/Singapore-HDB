# import dash_html_components as html
from dash import html
from navbar import create_navbar

nav = create_navbar()

# header = html.H3(f'User Chose: {path}')


def create_page_search_results(path):
    layout = html.Div([
        nav,
        html.H3(f'User Chose: {path}'),
    ])
    return layout
