# import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html, dcc
from navbar import create_navbar, create_footer
from app import app

nav = create_navbar()
discloser, footer = create_footer()

@app.callback(
    Output('address_search_output_test', 'children'),
    Input('submit_address_search', 'n_clicks'),
    State('address_search_input', 'value'),
    State('flat_type_search_input', 'value'),
    State('floor_search_input', 'value'),
    State('sq_m_search_input', 'value')
)
def update_output(n_clicks, address, flat_type, floor, sq_m):
    output_string = f"ADDRESS SEARCH: {address}\n FLAT TYPE: {flat_type}\nFLOOR: {floor}\nSQ METERS: {sq_m}"
    return output_string


def create_page_explore():
    layout = html.Div([
        nav,
        html.Div([dcc.Markdown("Explore Page")], style={'margin': '5% 10% 5% 10%'}),
        discloser,
        footer

    ]
    )

    return layout

