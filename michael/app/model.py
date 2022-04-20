import pandas as pd
import pickle
import matplotlib.pyplot as plt
import re
import xgboost
import io
import base64
from datetime import datetime
from geopy.geocoders import Nominatim
from database_helpers import DatabaseHelpers


# import shap for interpretation
import shap # v0.39.0
shap.initjs()


def predict_price(model_loc, object_id_loc, prediction_df):
    # load model from file
    model = pickle.load(open(model_loc, "rb"))

    # predict values
    prediction = model.predict(prediction_df)

    # update dataframe columns names for printing in SHAP

    # dictionary created from database conservation areas
    object_id_dict = pickle.load(open(object_id_loc, 'rb'))

    # get the current columns
    columns = prediction_df.columns.tolist()
    columns = [x for x in columns if x.startswith('dist_to_con_area_id_')]

    # get con_area_id which maps to objectid
    idxs = [int(re.findall(r'\d+', x)[0]) for x in columns]

    columns_to_display = {}

    # get a dictionary of the columns to display and update dataframe
    for id, col_name in zip(idxs, columns):
        columns_to_display[col_name] = 'dist_to_'+object_id_dict[id]
    prediction_df.rename(columns=columns_to_display,inplace=True)

    # get SHAP waterfall
    buf = io.BytesIO()
    plt.clf()
    plt.rc('font', size=10)
    plt.xticks(fontsize=10)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(prediction_df)

    fig = shap.plots.waterfall(shap_values[0], max_display=15, show=False)
    f = plt.gcf()
    # f.set_figheight(10)
    # f.set_figwidth(5)

    plt.savefig(buf, format='png', bbox_inches="tight", transparent=True)
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("utf8")
    fig = "data:image/png;base64,{}".format(data)


    # fig = shap.plots.waterfall(shap_values[0])
    # shap_html = f"<head>{shap.getjs()}</head><body>{fig.html()}</body>"

    # plt.savefig('prediction.png',bbox_inches='tight',transparent=True,dpi=500)

    return prediction, fig


def prep_data_for_model(address, flat_type, df, sq_m):
    geolocator = Nominatim(user_agent="http://127.0.0.1:8050/")
    location = geolocator.geocode(address.replace('-', ' '), namedetails=True)
    towns_dict = DatabaseHelpers.towns_dict
    if flat_type != "1-Room":
        # If flat_type isn't 1 bedroom add 1 to which town the address is in
        town_key = f"town_{location.raw['display_name'].split(', ')[3].lower().replace(' ', '_')}"
        if town_key in towns_dict.keys():
            towns_dict[town_key] = 1
        if flat_type:
            towns_dict[f"flat_type_{flat_type.lower().replace(' ', '_').replace('-', '_')}"] = 1

    flat_type_convert = {'1-Room': 1, '2-Room': 2, '3-Room': 3, '4-Room': 4, '5-Room': 5,
                         'Multi Generation': 5, 'Executive': 5}

    df.loc[0, 'n_rooms'] = flat_type_convert[flat_type]
    print(f"Data Prep: {df.loc[0, 'n_rooms']}")
    # If sq_m is an empty string just use floor_area_sqm that's in the results table
    #___________________________________________________________________________________________________________
    # if sq_m != '':
    #     df.loc[0, 'floor_area_sqm'] = int(sq_m)
    # df.loc[0, 'remaining_lease_years'] = (
    #         df.loc[0, 'remaining_lease_years'] - (datetime.now().year - df['month'].dt.year)).values
    # print(f"Remaining Lease Years: {(df.loc[0, 'remaining_lease_years'] - (datetime.now().year - df['month'].dt.year)).values}")
    #___________________________________________________________________________________________________________
    # print((datetime.now().year - df['month'].dt.year).values)
    df = df.merge(pd.DataFrame(towns_dict, index=[0]), right_index=True, left_index=True)
    df = df[DatabaseHelpers.model_must_have]

    return df
