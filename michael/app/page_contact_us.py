# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar, create_footer

nav = create_navbar()
discloser, footer = create_footer()
header = html.H1('Contact Us')


bio_text = \
"""
___  
## Tom Bresee  

[LinkedIn](https://www.linkedin.com/in/tombresee/) | [GitHub](https://github.com/tombresee) | tbresee@umich.edu
___  
## Michael McManus  

[LinkedIn](https://www.linkedin.com/in/michael-mcmanus/) | [GitHub](https://github.com/mcmanus-git) | [Medium](https://medium.com/@mcmanus_data_works) | msmcmanu@umich.edu  

___  
## Stuart Ong  

[LinkedIn](#) | [GitHub](#)    

"""

def create_page_contact_us():
    layout = html.Div([
        nav,
        html.Div([header], style={'margin': '5% 10% 5% 10%', 'textAlign': 'center'}),
        html.Div([dcc.Markdown(bio_text)], style={'margin': '5% 10% 5% 10%'}),
        footer
    ])
    return layout
