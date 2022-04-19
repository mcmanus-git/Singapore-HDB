from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from navbar import *

nav = create_navbar()
discloser, footer = create_footer()

dataset_page_content = \
"""# Dataset Attribution  

All data sources derived from [data.gov/sg](https://data.gov.sg/) during the months of March and April in the year 2022 under the terms of the [Singapore Open Data Licence version 1.0](https://data.gov.sg/open-data-licence)  


## Datasets Used in this Analysis

### E
- [Eating Establishments](https://data.gov.sg/dataset/eating-establishments)
### F
- [Fire Stations](https://data.gov.sg/dataset/fire-stations)
### H
- [Hawker Centres](https://data.gov.sg/dataset/hawker-centres)
- [HDB Carpark Information](https://data.gov.sg/dataset/hdb-carpark-information)
- [HDB Property Information](https://data.gov.sg/dataset/hdb-property-information)
- [Hotels](https://data.gov.sg/dataset/hotels)  
- [HDB Resale Price Index](https://data.gov.sg/dataset/hdb-resale-price-index)
### K
- [Kindergartens](https://data.gov.sg/dataset/kindergartens)
### L
- [LTA MRT Station Exit](https://data.gov.sg/dataset/lta-mrt-station-exit)
### M
- [Master Plan 2019 Planning Area Boundary](https://data.gov.sg/dataset/master-plan-2019-planning-area-boundary-no-sea)
### N
- [NParks Parks](https://data.gov.sg/dataset/nparks-parks)
### P
- [Parks](https://data.gov.sg/dataset/parks)
- [Pre-Schools Location](https://data.gov.sg/dataset/pre-schools-location)
- [Private Education Institutions](https://data.gov.sg/dataset/private-education-institutions) 
### S
- [School Directory and Information](https://data.gov.sg/dataset/school-directory-and-information)
- [SDCP MRT Station Point](https://data.gov.sg/dataset/sdcp-mrt-station-point)
- [Singapore Police Force Establishments](https://data.gov.sg/dataset/singapore-police-force-establishments)
- [Supermarkets](https://data.gov.sg/dataset/supermarkets)








 



"""

def create_datasets_page():


    layout = html.Div([
        nav,
        html.Div([
            dcc.Markdown(dataset_page_content)
        ], style={'margin': '5% 10% 0% 10%'})
    ])


    return layout