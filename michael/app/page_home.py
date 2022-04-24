from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import State
from navbar import create_navbar, create_footer
from app import app
from dash.dependencies import Input, Output
import time
from geopy.geocoders import Nominatim

# Note to self:
# Margin Top, Right, Bottom, Left
# 4459 33 TELOK BLANGAH WAY

nav = create_navbar()
discloser, footer = create_footer()


def create_page_home(sg_base_map):
    layout = html.Div([
        nav,
        html.Div([dcc.Graph(figure=sg_base_map)]),

        html.Div([
            html.Div([
                dcc.Input(id='address_search_input', type='text', placeholder='Enter Address', debounce=False, style=dict(width='300px'))
            ], style={'display': 'inline-block', 'margin': '0% 0% 0% 0%'}
            ),
            html.Div([
                dcc.Dropdown(['1 Room', '2 Room', '3 Room', '4 Room', '5 Room', 'Multi Generation', 'Executive'], placeholder='Rooms', id='flat_type_search_input'),
            ], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin': '0% 1% 0% 1%', 'width': '20%'}
            ),
            html.Div([
                dcc.Dropdown([i for i in range(1, 52)], placeholder='Floor',  id='floor_search_input'),
            ], style={'display': 'inline-block', 'vertical-align': 'middle', 'margin': '0% 1% 0% 1%', 'width': '10%'}
            ),
            html.Div([
                dcc.Input(id='sq_m_search_input', type='text', placeholder='Square Meters', debounce=True)
            ], style={'display': 'inline-block', 'margin': '0% 1% 0% 1%'}
            ),
            html.Div([
                dbc.Button(id='submit_address_search', n_clicks=0, children='Submit', color='success',
                           style={'display': 'inline-block'})#, href=f"/search-results")
            ], style={'display': 'inline-block', 'margin': '0% 0% 0% 1%'}
            ),
            html.Br(),
            html.Br(),
            html.Div(id='address_search_output'),
            html.Br(),
            html.Br(),
            html.Div([html.H3("HDBestimate", style={'text-transform': 'none'}),
                      dcc.Markdown("""  
Often, we purchase our home at the whims of the market without clear insights into what is driving the cost. 
The lack of pricing transparency becomes more apparent when looking at HDB resale flats which generally are of similar 
size, layout and features across flat types, yet we observe significantly varying transaction values. Further 
compounding this is the fact that HDB flats typically come with a 99-year lease, yet some of the most expensive 
transactions have been those of older units with shorter remaining lease terms. Outside of economic factors, 
location and proximity to places of interest are key drivers of resale price and we have built HDBestimate 
with the goal of using machine learning techniques to help purchasers gain insight into the effect location and other 
flat features can have on their unit’s cost. *Enter your flat information above to get started!*
        """),
                      html.Br(),
                      html.H3("Explore", style={'text-transform': 'none'}),
                      dcc.Markdown("""Unfamiliar with Singapore? That's ok! Check out our [Explore Page](/explore)."""),
                      html.Br(),
                      html.H3("How did we do it?", style={'text-transform': 'none'}),
                      dcc.Markdown("""Interested in knowing more about how HDBestimate works to deliver transparency in the HDB market? 
Head on over to the [Blog Page](/blog) and take a closer look.""",
                                   style={"white-space": "pre"},
                                   dangerously_allow_html=True)
                      ]),
        ],
            style={'margin': '0% 10% 5% 10%'}),
        discloser,
        footer
    ])
    return layout


@app.callback(
    Output('address_search_output', 'children'),
    Input('submit_address_search', 'n_clicks'),
    State('address_search_input', 'value'),
    State('flat_type_search_input', 'value'),
    State('floor_search_input', 'value'),
    State('sq_m_search_input', 'value'),
    prevent_initial_call=True
)
def get_address_information(n_clicks, address, flat_type, floor, sq_m):
    time.sleep(1)

    geolocator = Nominatim(user_agent="http://127.0.0.1:8050/")
    location = geolocator.geocode(address, namedetails=True)

    if address is None:
        address = ''
    elif flat_type is None:
        flat_type = ''
    elif floor is None:
        floor = ''
    elif sq_m is None:
        sq_m = ''


    d = location.address.split(', ')
    address = f"{d[0]}-{d[1].replace(' ', '-')}-{d[3].replace(' ', '-')}-{d[-1]}"
    search_results = html.Div([html.H3('Search Results', style={'color': '#4ABF72'}),
                               html.Br(),
                               dcc.Markdown(f"""[{location.address}](/search-results/{address}%{location.longitude}%{location.latitude}%{flat_type.replace(' ', '-')}%{floor}%{sq_m})
    """)], style={'color': 'red'})

    return search_results
