# import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html, dcc
from navbar import create_navbar
from app import app

nav = create_navbar()


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
        html.Div([
        html.Div([
            dcc.Input(id='address_search_input', type='text', placeholder='Enter Address', debounce=False, style=dict(width='300px'))
        ], style={'display': 'inline-block', 'margin': '0% 0% 0% 2%'}
        ),
            html.Div([
                dcc.Dropdown(['1 Room', '2 Room', '3 Room', '4 Room', '5 Room', 'Multi-Generation', 'Executive'], placeholder='Rooms', id='flat_type_search_input'),
            ], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin': '0% 1% 0% 1%', 'width': '25%'}
            ),
            html.Div([
                dcc.Dropdown([i for i in range(1, 52)], placeholder='Floor',  id='floor_search_input'),
            ], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin': '0% 1% 0% 1%', 'width': '10%'}
            ),
            html.Div([
                dcc.Input(id='sq_m_search_input', type='text', placeholder='Square Meters', debounce=True)
            ], style={'display': 'inline-block', 'margin': '0% 2% 0% 2%'}
            ),
            html.Div([
                dbc.Button(id='submit_address_search', n_clicks=0, children='Submit', style={'display': 'inline-block'})
            ], style={'display': 'inline-block', 'margin': '0% 2% 0% 2%'}
            ),
            html.Br(),
            html.Br(),
            html.Div(id='address_search_output_test')
            ], style={'margin': '5% 10% 5% 10%'}
            ),

    ]
    )

    return layout

