# import dash_html_components as html
from dash import html
from navbar import create_navbar
from maps import create_search_results_map
from dash import dcc
from database_helpers import DatabaseHelpers
import geopandas as gpd

nav = create_navbar()


def get_address_details(pathname):
    pathname = pathname.strip("/")

#     address_geo_search = f"""SELECT *
# FROM hdb_property_info a
# LEFT JOIN sg_buildings_postal_geo b
# ON CONCAT(a.blk_no,' ',a.street) = CONCAT(b.blk_no,' ',b.short_r_name)
# where building_id = {pathname};"""

    address_geo_search = f"""
    select * from resale_location_features
    where building_id = {pathname}
    order by month desc
    limit 1;
    """

    engine = DatabaseHelpers.engine
    with engine.connect() as cnxn:
        df = gpd.read_postgis(address_geo_search, cnxn, geom_col="geometry")

    return df


def search_results_text(df):
    results_string = dcc.Markdown(f"""
### {df['address'].values[0]}
    
#### Most recent transaction information  
Date: {df['month'].dt.strftime('%B %d, %Y')[0]}  
Rooms: {df['n_rooms'].values[0]}  
Sale Price: ${df['resale_price_norm'].values[0]:,.2f}  
     
    """)
    return results_string


def create_page_search_results(path):

    path = path.strip("/")

    df = get_address_details(path)
    page_results_string = search_results_text(df)

    layout = html.Div([
        nav,
        html.Div([dcc.Graph(figure=create_search_results_map(df))
                  ],
                 style={'margin': '0% 5% 0% 5%'}
                 ),
        html.Div([page_results_string],
                 style={'margin': '0% 10% 0% 10%'}
                 )
        # html.Div([dcc.Graph(figure=create_search_results_map(df))]
        # html.H3(f"Showing results for {df['address_to_match'].values[0]}")
        #          )
    ])
    return layout
