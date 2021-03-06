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
    # print(sq_m)
    results_string = f"""
## Estimated Resale:  ${(a * int(sq_m) * remaining_lease_years):,.2f}
${a * remaining_lease_years:,.2f} per square meter  
{remaining_lease_years} remaining lease years  
(${a:,.2f} per square meter per lease year predicted price)  """

    historical_info_string = \
        f"""#### Model Explanation  
Our model predicts price per square meter per lease year using 15 years of resale data with an R2 of 0.73. Using this 
output, we convert price per square meter per lease year to total estimated resale value using HDB flat size and age. 
The waterfall plot above highlights the top 15 features which have the largest effect on resale price in contrast to 
the average resale price predicted by our model using SHAP values. The blue bars represent those features which our 
model predicts as having a negative effect, while the red bars represent those features our model predicts as having a 
positive effect on resale price when compared to the average predicted price of our model. When comparing our predicted 
resale price to historic transactions, a higher predicted transacted price suggests that the purchaser is overpaying, 
while a lower predicted transacted price suggest the purchaser is underpaying.  

#### Most Recent Transaction Comparison
The last property sold at this address was a {n_rooms} bedroom sold in {most_recent_transaction_date} for ${float(most_recent_resale):,.2f}
    """

    return results_string, historical_info_string


def create_page_search_results(pathname):
    # Get variables out of path name
    search_params_from_url = pathname.strip("/search-results").split("%")

    address = search_params_from_url[0]
    lon = search_params_from_url[1]
    lat = search_params_from_url[2]
    flat_type = search_params_from_url[3]
    storey = search_params_from_url[4]
    sq_m = search_params_from_url[5]

    features = DatabaseHelpers.features

    df = get_address_details(lon, lat, features)

    search_results_map = create_search_results_map(df)

    remaining_lease_years = df['remaining_lease_years'].values[0]
    df_sqr_m = df['floor_area_sqm'].values[0]
    most_recent_resale = df['resale_price'].values
    most_recent_transaction_date = df['month'].dt.strftime('%B, %Y')[0]
    number_rooms = int(df['n_rooms'].values[0])
    # print(f"Flat type going into model: {flat_type}")
    df_model = prep_data_for_model(address, flat_type, df, storey, sq_m)

    path = 'assets/model_xgb.pickle.dat'
    objec_id_loc = 'assets/object_id_dict.pickle'

    a, b = predict_price(path, objec_id_loc, df_model)

    results_text, historical_text = search_results_text(df, a, address, remaining_lease_years, sq_m, df_sqr_m,
                                                        most_recent_transaction_date, most_recent_resale, number_rooms)

    layout = html.Div([
        nav,
        html.H1(f"{address.replace('-', ' ')}", style={'textAlign': 'center', 'margin': '5% 0% 0% 0%'}),
        html.Div([dcc.Graph(figure=search_results_map)
                  ],
                 style={'margin': '0% 5% 0% 5%'}
                 ),
        # html.Div(id='address_search_output'),
        html.Div([html.Div([
            html.Br(),
            html.Br(),
            html.Div([dcc.Markdown(results_text)], style={'margin': '0% 0% 0% 7%'}),
            html.Br(),
            html.Br(),
            html.Div([dcc.Markdown("""### Features Impacting Resale Price""")],
                     style={'margin': '0% 0% 0% 7%', 'textAlign': 'center'}),
            html.Div([html.Img(src=b, style={'height': '100%', 'width': '100%'})]),
            html.Br(),
            html.Br(),
            html.Div([dcc.Markdown(historical_text)], style={'margin': '0% 0% 0% 0%'}),
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
