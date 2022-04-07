def get_features_targets(df,list_of_cols_to_ohe):
    '''
    Function to performing general cleaning/remove bloat for dataframe pulled from 
    the database for use downstream in models

    Input: Dataframe 
    Output: Dataframe

    1. Drop duplicate transactions on transaction_id - some joins have multiple buildings
    2. Check and drop NAN rows with no lat/lon match
    3. Remove excess columns - ids
    4. Fill remaining NANs with 0 - these NANs have location features with no match
    5. Convert Catergorical Columns using OneHotEncoding - drops first to prevent multicolinearity
    '''

    # libs used
    import pandas as pd
    import numpy as np
    from sqlalchemy import create_engine
    from MyCreds.mycreds import Capstone_AWS_RO       #from local site-packages
    from sklearn.preprocessing import OneHotEncoder

    # create connection to engine for onehotencoding labels
    engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_RO.username}:{Capstone_AWS_RO.password}@{Capstone_AWS_RO.host}/Capstone', echo=False)
    sql_alc_cnxn = engine.connect()

    def do_ohe(df,field):
        '''
        Sub-function to perform OneHotEncoding
        Libs loaded upfront
        '''
        # get categories for column - for OneHotEncoding
        sql_query = f'''
        select distinct({field}) from resale_price_norm
        '''
        unique_val = pd.read_sql(sql_query, sql_alc_cnxn)
        # clean strings
        unique_val[field] = unique_val[field].str.lower().str.replace('-','_').str.replace(' ','_').str.replace('/','_')
        # get unique values 
        unique_val = list(set(unique_val[field].tolist()))
        # sort list - sort function is in place
        unique_val.sort()
        # convert to array
        unique_val = np.array(unique_val)
        
        # initialize a OHE
        ohe = OneHotEncoder(drop='first',handle_unknown='error').fit(unique_val.reshape(-1,1))

        # get column and transform
        to_encode = np.array(df[field].tolist())
        transformed = ohe.transform(to_encode.reshape(-1,1)).toarray()
        
        # join to original dataframe
        df = df.reset_index(drop=True)
        df = pd.concat([df,pd.DataFrame(transformed,columns=[field+'_'+x for x in ohe.categories_[0][1:]])],axis=1)

        # drop column
        df = df.drop(columns=[field])
        return df
    

    # clean town - for OneHotEncoding
    df['town'] = df['town'].str.lower().str.replace('-','_').str.replace(' ','_').str.replace('/','_')
    # clean flat_model - for OneHotEncoding
    df['flat_model'] = df['flat_model'].str.lower().str.replace('-','_').str.replace(' ','_').str.replace('/','_')
    # clean flat_type - for OneHotEncoding
    df['flat_type'] = df['flat_type'].str.lower().str.replace('-','_').str.replace(' ','_').str.replace('/','_')

    # identify excess columns not required for models
    columns_to_drop = ['transaction_id',
                        'month',
                        'block',
                        'street_name',
                        'address',
                        'storey_range',
                        'lease_commence_date',
                        'remaining_lease',
                        'remaining_lease_months',
                        'resale_price',
                        'price_per_sq_ft',
                        'price_per_sq_m',
                        'price_per_sq_ft_per_lease_yr',
                        'price_per_sq_m_per_lease_yr',
                        'flat_type',
                        ]    
    # identify categorical columns
    all_cat_columns = ['town',
                       'flat_model',
                       'flat_type'
                      ]
    

    # for dealing with duplicate transaction
    df = df.drop_duplicates()

    # check if dataframe contains added location features
    # resale_price _norm - which has no added location data contains 26 cols
    # treatment of columns to drop and cat_columns change if contain location features

    if df.shape[1] != 27:
        # first remove rows that no match on address - just a check
        # not if not looking at location features, no need to check this
        df = df.dropna(subset=['latitude','longitude'])
        
        # location features added - drop excess id columns as well
        # no excess_id columns
        additional_ids  = ['conservation_loc_id',
                           'expressway_loc_id',
                           'fire_loc_id',
                           'hawker_loc_id',
                           'healthcare_loc_id',
                           'malls_loc_id',
                           'park_major_loc_id',
                           'park_minor_id',
                           'poi_loc_id',
                           'police_loc_id',
                           'preschool_loc_id',
                           'primary_loc_id',
                           'secondary_loc_id',
                           'supermarket_loc_id',
                           'taxi_loc_id',
                           'transit_exit_loc_id',
                           'transit_station_loc_id',
                           'waterbody_loc_id',
                           'wetmarket_loc_id',
                           'busstop_loc_id',
                          ]
        additional_cols = ['building_id',
                           'address_buildings',
                           'blk_no',
                           'building',
                           'latitude',
                           'longitude',
                           'longtitude',
                           'postal',
                           'road_name',
                           'short_r_name',
                           'searchval',
                           'geometry',
                           'x',
                           'y',
                           ]
        # if contains location features, drop the additional cols/id
        columns_to_drop = columns_to_drop + additional_ids + additional_cols + [x for x in all_cat_columns if x not in list_of_cols_to_ohe]
    else:
        columns_to_drop = columns_to_drop + [x for x in all_cat_columns if x not in list_of_cols_to_ohe]

    # drop excess columns
    df = df.drop(columns=columns_to_drop)

    # fill remaining NaNs with 0 - remaining would be location features 
    # count or sum score within radius and hence fill with zero 
    # if distance to is NaN we need to fill with a bigger number
    df = df.fillna(0)

    # print(df.shape)

    # lastly perform onehotencoding for all cat_columns
    for cat in list_of_cols_to_ohe:
        df = do_ohe(df,cat)


    return df

if __name__ == '__main__':
    print('Hi there! - update your script!')