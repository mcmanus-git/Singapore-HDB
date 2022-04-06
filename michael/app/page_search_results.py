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

    address_geo_search = f"""SELECT *
FROM hdb_property_info a
LEFT JOIN sg_buildings_postal_geo b
ON CONCAT(a.blk_no,' ',a.street) = CONCAT(b.blk_no,' ',b.short_r_name)
where building_id = {pathname};"""

    engine = DatabaseHelpers.engine
    with engine.connect() as cnxn:
        df = gpd.read_postgis(address_geo_search, cnxn, geom_col="geometry")

    return df


def create_page_search_results(path):

    path = path.strip("/")

    df = get_address_details(path)

    layout = html.Div([
        nav,
        html.Div([html.H3(f"Showing results for {df['address_to_match'].values[0]}"),
                  dcc.Graph(figure=create_search_results_map(df))
                  ],
                 style={'margin': '5% 10% 10% 10%'}
                 ),
        # html.Div([dcc.Graph(figure=create_search_results_map(df))]
        #          )
    ])
    return layout
