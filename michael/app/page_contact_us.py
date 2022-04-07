# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar

nav = create_navbar()

header = html.H1('Contact Us')


bio_text = \
"""
___  
## Tom Bresee  
Tom is Tom  

___  
## Michael McManus  
Michael is an ass  
[LinkedIn](https://www.linkedin.com/in/michael-mcmanus/) [GitHub](https://github.com/mcmanus-git) [Medium](https://medium.com/@mcmanus_data_works)

___  
## Stuart Ong  
Rhymes with Pong  

"""

def create_page_contact_us():
    layout = html.Div([
        nav,
        html.Div([header], style={'margin': '5% 10% 5% 10%', 'textAlign': 'center'}),
        html.Div([dcc.Markdown(bio_text)], style={'margin': '5% 10% 5% 10%'})
    ])
    return layout
