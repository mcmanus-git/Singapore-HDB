from dash import html
from navbar import create_navbar, create_footer
from maps import create_search_results_map
from dash import dcc
from database_helpers import DatabaseHelpers
from model import predict_price, prep_data_for_model
import shap
from address_search import get_address_details

nav = create_navbar()
discloser, footer = create_footer()


def search_results_text(df, a, address, remaining_lease_years, sq_m, df_sqr_m, most_recent_transaction_date, most_recent_resale, n_rooms):
    a = float(a[0])
    if sq_m == '':
        sq_m = df_sqr_m
    print(sq_m)
    results_string = f"""
## Estimated Resale:  ${(a * int(sq_m) * remaining_lease_years):,.2f}
${a * remaining_lease_years:.2f} per square meter
{remaining_lease_years} remaining lease years
(${a:.2f} per square meter per lease year predicted price)  


#### Most Recent Transaction
The last property sold at this address was a {n_rooms} bedroom sold on {most_recent_transaction_date} for ${float(most_recent_resale):,.2f}
    """

    return results_string


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
    search_results_map = create_search_results_map(df)
    remaining_lease_years = df['remaining_lease_years'].values[0]
    df_sqr_m = df['floor_area_sqm'].values[0]
    most_recent_resale = df['resale_price'].values
    most_recent_transaction_date = df['month'].dt.strftime('%B %d, %Y')[0]
    number_rooms = int(df['n_rooms'].values[0])
    df = prep_data_for_model(address, flat_type, df, sq_m)

    path = 'assets/model_xgb.pickle.dat'
    objec_id_loc = 'assets/object_id_dict.pickle'

    a, b = predict_price(path, objec_id_loc, df)

    results_text = search_results_text(df, a, address, remaining_lease_years, sq_m, df_sqr_m, most_recent_transaction_date,
                                       most_recent_resale, number_rooms)

    layout = html.Div([
        nav,
        html.Div([dcc.Graph(figure=search_results_map)
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
                            html.Div([html.Img(src=b, style={'height': '100%', 'width': '100%'})]),
                            html.Br(),
                            html.Br(),
                            # dbc.Row([
                            #     dbc.Col(html.Div([dcc.Markdown(results_text)])),
                            #     dbc.Col(html.Div([html.Img(src=b, style={'height': '100%', 'width': '100%'})]))
                            # ]),
                            ],
                           style={'margin': '0% 10% 0% 10%'}
                           )
                  ]),
        discloser,
        footer
    ])
    return layout
