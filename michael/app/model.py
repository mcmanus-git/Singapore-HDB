import pandas as pd
import pickle
import matplotlib.pyplot as plt
import re
import xgboost
import io
import base64

# import shap for interpretation
import shap # v0.39.0
shap.initjs()


def predict_price(model_loc, object_id_loc, prediction_df):
    # load model from file
    model = pickle.load(open(model_loc, "rb"))

    # predict values
    prediction = model.predict(prediction_df)
    print(prediction)

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
    f.set_figheight(10)
    f.set_figwidth(5)



    plt.savefig(buf, format='png', bbox_inches="tight")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("utf8")
    fig = "data:image/png;base64,{}".format(data)


    # fig = shap.plots.waterfall(shap_values[0])
    # shap_html = f"<head>{shap.getjs()}</head><body>{fig.html()}</body>"

    print(type(fig))

    # plt.savefig('prediction.png',bbox_inches='tight',transparent=True,dpi=500)

    return prediction, fig
