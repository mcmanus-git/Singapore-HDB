import geopandas as gpd
from database_helpers import DatabaseHelpers


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
