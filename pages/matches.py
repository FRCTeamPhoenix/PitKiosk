from dash import Dash, dash_table, html
import pandas as pd
from collections import OrderedDict

data = OrderedDict(
    [
        ("Match Number", ["1", "2", "3", "4", "5", "6"]),
        ("Opponent", ["3333/Team Name", "4444/Team Name", "5555/Team Name", "7777/Team Name", "8888/Team Name", "9999/Team Name"]),
        ("Team Phoenix Points", [1000, 1000, 1000, 1000, 1000, 1000]),
        ("Winner", ["Team Phoenix", "Team Phoenix", "Team Phoenix", "Team Phoenix", "Team Phoenix", "Team Phoenix"]),
        ("Additional Points", ["Cooperition", "Coral RP", "Cooperition", "Auto RP", "Cooperition", "Barge RP"]),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 1) for (name, col_data) in data.items()])
)

layout = html.Div(dash_table.DataTable(
    id= "match-table",
    data= df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_action='none',
    style_table={'height': '250px', 'overflowY': 'auto'})
)