# import dash_html_components as html
from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to page 2!')


def create_page_blog():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
