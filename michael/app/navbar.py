import dash_bootstrap_components as dbc
import dash.html as html
from dash import dcc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Blog", href='/blog'),
                    dbc.DropdownMenuItem("Contact Us", href='/contact-us'),
                    dbc.DropdownMenuItem("Explore", href='/explore'),
                ],
            ),
        ],
        brand="Why-High",
        brand_href="/",
        sticky="top",
        # color='#D91800',
        color="success",  # Change this to change color of the navbar e.g. "primary", "secondary", "dark" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar


def create_footer():
    discloser = html.Div([dcc.Markdown('*Contains information from [datasets](/datasets) accessed throughout March\
    and April 2022 from {source of data} which is made available under the terms of the [Singapore Open Data Licence \
    version 1.0](https://data.gov.sg/open-data-licence)')], style={'margin': '10% 1% 0% 1%', 'font-size': '10px'})

    footer = html.Footer([html.Div([' ']), html.Div(['© 2022 WhyAxis'],
                                                    style={'margin': '0% 0% 0% 2%', 'font-size': '12px'}),
                          html.Div([' '])], style={'background-color': '#4ABF72', 'color': 'white', 'height': '50px', 'left': 0}
                                                   #'position': 'absolute', 'left': 0, 'bottom': 0, 'width': '100%', 'height': '50px'},

                         )

    return discloser, footer
