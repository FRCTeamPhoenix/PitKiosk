#necessary imports
import dash
from dash import html, dcc, dash_table
import pandas as pd

data = [
    {"ID": "1", "Part": "Motors", "Description": "Krakenx60's with Talon FX encoders"}, 
    {"ID": "2", "Part": "Robot Controller", "Description": "NI-roboRIO 2"}, 
    {"ID": "3", "Part": "Height", "Description": "3 feet, 5.5 inches"}, 
    {"ID": "4", "Part": "Weight", "Description": "108.2 pounds"}, 
    {"ID": "5", "Part": "Elevator", "Description": "GreyT Cascade Elevator, 3 Stage -(West Coast Products)"}, 
    {"ID": "6", "Part": "Autos", "Description": "We have 13,536 possible autos, and each can score 2 corals on L4, L3, or L2"}
]

df = pd.DataFrame(data)

layout = dash_table.DataTable(
                          id="table",
                          columns=[{"name": "Part", "id": "Part"},{"name": "Description", "id": "Description"}],
                          data=df.to_dict('records'),
                          style_table={'padding': '0', 'marginTop': '0px'},
                          style_cell={'padding': '10px','textAlign': 'left'},
                          style_header={'backgroundColor': '#d9534f','color': 'black', 'fontWeight': 'bold', 'textAlign': 'center'}
                          #style_data_conditional=[{'if': {'cell_id': 'Description'},'backgroundColor': '#d9534f', 'color': 'black'}]
)
#layout = html.Div (className="specs-container",  # Parent container with flex layout
 #   children=[
  #  html.H1("Robot Specifications"),
   # html.H2(className="specs-h2", children= "Motors"),
    #html.Ul(className= "specs-ul", children= [html.Li("Krakenx60's (with Talon FX encoders)")]),
    #html.H2(className="specs-h2", children= "Robot Controller"),
    #html.Ul(className= "specs-ul", children= [html.Li("NI-roboRIO 2")]), 
    #html.H2(className="specs-h2", children= "Height"),
   # html.Ul(className= "specs-ul", children= [html.Li("3 feet, 5.5 inches")]),
   # html.H2(className="specs-h2", children= "Weight"),
    #html.Ul(className= "specs-ul", children= [html.Li("108.2 pounds")]),
    #html.H2(className="specs-h2", children= "Elevator"),
    #html.Ul(className= "specs-ul", children=[html.Li("GreyT Cascade Elevator, 3 Stage - (West Coast Products)")]),
   # html.H2(className="specs-h2", children= "Autos"),
   # html.Ul(className= "specs-ul", children=[html.Li("We have 13,536 possible autos, and each can score 2 corals on L4, L3, or L2")])
#])
