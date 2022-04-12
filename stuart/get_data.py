def get_data(table, train_start_yr,train_end_yr,validation_start_yr,validation_end_yr,test_start_yr):
    '''
    Function to query database - start and end years are inclusive
    All years should be different
    '''

    import pandas as pd
    from sqlalchemy import create_engine
    from MyCreds.mycreds import Capstone_AWS_RO       #from local site-packages

    engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_RO.username}:{Capstone_AWS_RO.password}@{Capstone_AWS_RO.host}/Capstone', echo=False)
    sql_alc_cnxn = engine.connect()

    # get training data
    sql_query = f'''
    select * from {table}
    WHERE "month" > '{train_start_yr-1}-12-31 00:00:00'::timestamp
    AND "month" <= '{train_end_yr}-12-31 00:00:00'::timestamp
    '''
    print("Getting Training Data")
    train_df = pd.read_sql(sql_query, sql_alc_cnxn)
    print("Training Data Done")

    # get validate data
    sql_query = f'''
    select * from {table}
    WHERE "month" > '{validation_start_yr-1}-12-31 00:00:00'::timestamp
    AND "month" <= '{validation_end_yr}-12-31 00:00:00'::timestamp
    '''
    print("Getting Validate Data")
    validate_df = pd.read_sql(sql_query, sql_alc_cnxn)
    print("Validate Data Done")

    # get test data
    sql_query = f'''
    select * from {table}
    WHERE "month" > '{test_start_yr-1}-12-31 00:00:00'::timestamp
    '''
    print("Getting Test Data")
    test_df = pd.read_sql(sql_query, sql_alc_cnxn)
    print("Test Data Done")

    return train_df,validate_df,test_df

if __name__ == '__main__':
    print('Hi there! - update your script!')