# import dash_html_components as html
from dash import html
import dash_bootstrap_components as dbc
from navbar import create_navbar
from maps import create_search_results_map, create_sg_base_map
from dash import dcc
from database_helpers import DatabaseHelpers
import geopandas as gpd
from geopy.geocoders import Nominatim
from datetime import datetime
import pandas as pd
from model import predict_price
import shap

nav = create_navbar()


def get_address_details(lon, lat, features):
    sql = f"""select {", ".join(features)},
    st_setsrid(st_makepoint({lon}, {lat}), 4326)::geography <-> geometry::geography as distance
    from resale_location_features
    order by distance asc, month desc
    limit 1;"""

    engine = DatabaseHelpers.engine

    with engine.connect() as cnxn:
        df = gpd.read_postgis(sql, cnxn, geom_col='geometry')

    return df


def prep_data_for_model(address, flat_type, df, sq_m):
    geolocator = Nominatim(user_agent="http://127.0.0.1:8050/")
    location = geolocator.geocode(address.replace('-', ' '), namedetails=True)
    towns_dict = DatabaseHelpers.towns_dict
    if flat_type != 1:
        # If flat_type isn't 1 bedroom add 1 to which town the address is in
        town_key = f"town_{location.raw['display_name'].split(', ')[3].lower().replace(' ', '_')}"
        if town_key in towns_dict.keys():
            towns_dict[town_key] = 1
        if flat_type:
            towns_dict[f"flat_type_{flat_type.lower().replace(' ', '_').replace('-', '_')}"] = 1
    # If sq_m is an empty string just use floor_area_sqm that's in the results table
    if sq_m != '':
        df.loc[0, 'floor_area_sqm'] = int(sq_m)
    df.loc[0, 'remaining_lease_years'] = (
            df.loc[0, 'remaining_lease_years'] - (datetime.now().year - df['month'].dt.year)).values
    # print((datetime.now().year - df['month'].dt.year).values)
    df = df.merge(pd.DataFrame(towns_dict, index=[0]), right_index=True, left_index=True)
    df = df[DatabaseHelpers.model_must_have]

    return df


def search_results_text(df, a, address, sq_m):
    a = float(a[0])
    if sq_m == '':
        sq_m = df['floor_area_sqm'].values
    results_string = f"""
## Estimated Resale:  
- ${(a * int(sq_m) * int(df['remaining_lease_years'].values[0])):,.2f}
- ${a:.2f} per square meter
    """
    # Date: {df['month'].dt.strftime('%B %d, %Y')[0]}
    # Sale Price: ${df['resale_price_norm'].values[0]:,.2f}
    # print(df['remaining_lease_years'].values)
    return results_string


def model_results_text(df):
    results_text = f"""# Model Results  
#### Current Value: $1.5 M  
\n\n
#### Most Relevant Features:  
\n\n
    (chart)
    """

    return results_text


def create_page_search_results(pathname):
    # Get variables out of path name
    search_params_from_url = pathname.strip("/search-results").split("%")

    address = search_params_from_url[0]
    lon = search_params_from_url[1]
    lat = search_params_from_url[2]
    flat_type = search_params_from_url[3]
    sq_m = search_params_from_url[4]

    features = DatabaseHelpers.features

    df = get_address_details(lon, lat, features)
    df = prep_data_for_model(address, flat_type, df, sq_m)

    path = 'assets/model_xgb.pickle.dat'
    objec_id_loc = 'assets/object_id_dict.pickle'

    a, b = predict_price(path, objec_id_loc, df)

    results_text = search_results_text(df, a, address, sq_m)

    layout = html.Div([
        nav,
        # html.Div([dcc.Graph(figure=create_search_results_map(df))
        html.Div([dcc.Graph(figure=create_sg_base_map())
                  ],
                 style={'margin': '0% 5% 0% 5%'}
                 ),
        # html.Div(id='address_search_output'),
        html.Div([html.Div([html.H1(f"{address.replace('-', ' ')}", style={'textAlign': 'center'}),
                            html.Br(),
                            html.Br(),
                            html.Div([dcc.Markdown(results_text)], style={'margin': '0% 0% 0% 7%'}),
                            html.Br(),
                            html.Br(),
                            html.Div([html.Img(src=b, style={'height': '70%', 'width': '70%'})]),
                            html.Br(),
                            html.Br(),
                            # dbc.Row([
                            #     dbc.Col(html.Div([dcc.Markdown(results_text)])),
                            #     dbc.Col(html.Div([html.Img(src=b, style={'height': '100%', 'width': '100%'})]))
                            # ]),
                            ],
                           style={'margin': '0% 10% 0% 10%'}
                           )
                  ])
    ])
    return layout
