import dash_bootstrap_components as dbc


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
                    dbc.DropdownMenuItem("Page 3", href='/page-3'),
                ],
            ),
        ],
        brand="Why-High",
        brand_href="/",
        sticky="top",
        color='#D91800',#"primary",  # Change this to change color of the navbar e.g. "primary", "secondary", "dark" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
