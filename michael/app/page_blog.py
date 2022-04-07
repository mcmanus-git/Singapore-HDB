# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar

nav = create_navbar()

# header = html.H3('Welcome to page 2!')


blog_text = \
"""
# Blog  
It was the best of times.  It was the worst of times.  

# Abstract  
We used data 
___  

# Motivation  
Fame and fortune
  
  

# Data Used  
Lots of free stuff

# Analysis Methods  
None that I know of.

# Results  
Poor

# Further Research  
Is the hokie pokie really what it's all about?  

# Statment of Work  
What work?


"""


def create_page_blog():
    layout = html.Div([
        nav,
        html.Div([dcc.Markdown(blog_text)], style={'margin': '5% 10% 5% 10%'}),
    ])
    return layout
