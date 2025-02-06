#necessary imports
import dash
from dash import html, dcc

layout = html.Div ([
    html.H1("Robot Specifications"),
    html.H2("Motors"),
    html.Ul(id = "motors", children= [html.Li("Krakenx60's (with Talon FX encoders)")]),
    html.H2("Robot Controller"),
    html.Ul(id = "rio", children= [html.Li("NI-roboRIO 2")]), 
    html.H2("Power Distribution Hub?"),
    html.H2("Elevator"),
    html.Ul(id = "elevator-specs", children=[html.Li("GreyT Cascade Elevator, 3 Stage - (West Coast Products)")])
])
