# import dash_html_components as html
from dash import html, dcc
from navbar import create_navbar, create_footer

nav = create_navbar()
discloser, footer = create_footer()


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

    # with open('../app/assets/Blog HTML Test.html') as file:
    with open('assets/capstone.html') as file:
        lines = file.readlines()

    lines = "".join(lines)

    layout = html.Div([
        nav,
        # html.Div([dcc.Markdown(blog_text)], style={'margin': '5% 10% 5% 10%'}),
        html.Div([html.Iframe(srcDoc=lines, height="27000px", width="100%")], style={'margin': '0% 10% 0% 5%'}),
        discloser,
        footer
    ])
    return layout
