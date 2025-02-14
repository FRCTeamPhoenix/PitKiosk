from dash import Dash, dash_table, dcc, html
import pandas as pd


params = [
    'Weight', 'Torque', 'Width', 'Height',
    'Efficiency', 'Power', 'Displacement'
]

layout = html.Div([
    dash_table.DataTable(
        id='table-editing-simple',
        columns=(
            [{'id': 'Model', 'name': 'Model'}] +
            [{'id': p, 'name': p} for p in params]
        ),
        data=[
            dict(Model=i, **{param: 0 for param in params})
            for i in range(1, 5)
        ],
        editable=False 
    ),
    dcc.Graph(id='table-editing-simple-output')
])