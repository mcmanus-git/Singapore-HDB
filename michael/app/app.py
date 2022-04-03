import dash
import dash_bootstrap_components as dbc

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# BOOTSTRAP, CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI, ZEPHYR.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.LUX,
                                      'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'])
# app.layout(fluid=True, className="dbc")
server = app.server
