# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar, create_footer

nav = create_navbar()
discloser, footer = create_footer()
header = html.H1('Contact Us')


line_break_text = """___  """

bio_text_tom = \
"""

## Tom Bresee  

[LinkedIn](https://www.linkedin.com/in/tombresee/) | [GitHub](https://github.com/tombresee) | tbresee@umich.edu
"""

bio_text_michael = \
"""

## Michael McManus  
Michael is a Master's Student at the University of Michigan School of Information pursuing his degree in Applied Data Science.  
He works as a Senior Data Analyst at Consumers Energy and loves all things data.    

"""

contacts_michael = """[LinkedIn](https://www.linkedin.com/in/michael-mcmanus/) | [GitHub](https://github.com/mcmanus-git) | [Medium](https://medium.com/@mcmanus_data_works) | msmcmanu@umich.edu"""

bio_text_stuart = \
"""

## Stuart Ong  

[LinkedIn](https://www.linkedin.com/in/stuart-ong) | [GitHub](https://github.com/stuartong)    



"""

def create_page_contact_us():
    layout = html.Div([
        nav,
        html.Div([header], style={'margin': '5% 10% 5% 10%', 'textAlign': 'center'}),
        html.Div([dcc.Markdown(line_break_text)], style={'margin': '5% 10% 5% 10%'}),
        html.Div([dcc.Markdown(bio_text_tom)], style={'margin': '5% 10% 5% 10%'}),
        html.Br(),
        html.Div([dcc.Markdown(line_break_text)], style={'margin': '5% 10% 5% 10%'}),
        html.Div([dcc.Markdown(bio_text_michael)], style={'margin': '5% 10% 0% 10%'}),
        html.Br(),
        html.Div([dcc.Markdown(contacts_michael)], style={'margin': '0% 10% 0% 10%'}),
        html.Div([dcc.Markdown(line_break_text)], style={'margin': '5% 10% 5% 10%'}),
        html.Div([dcc.Markdown(bio_text_stuart)], style={'margin': '5% 10% 5% 10%'}),
        html.Br(),
        html.Div([dcc.Markdown(line_break_text)], style={'margin': '5% 10% 5% 10%'}),
        footer
    ])
    return layout
