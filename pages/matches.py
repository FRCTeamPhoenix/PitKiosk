from dash import Dash, dash_table, html
import pandas as pd
from collections import OrderedDict


layout = html.Div([
    html.H1("Match Information on Blue Alliance"),
    html.Img(className= "qr_code", src="/assets/black_qr.png")
])

