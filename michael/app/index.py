# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
from home import create_page_home
from page_blog import create_page_blog
from page_3 import create_page_3
from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/blog':
        return create_page_blog()
    if pathname == '/page-3':
        return create_page_3()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.title = "WhyHigh"
    app.run_server(debug=True)
