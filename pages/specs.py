#necessary imports
import dash
from dash import html, dcc

layout = html.Div ([
    html.H1("Robot Specifications"),
    html.H2("Motors"),
    html.Ul(className= "specs-ul", children= [html.Li("Krakenx60's (with Talon FX encoders)")]),
    html.H2("Robot Controller"),
    html.Ul(className= "specs-ul", children= [html.Li("NI-roboRIO 2")]), 
    html.H2("Height"),
    html.Ul(className= "specs-ul", children= [html.Li("3 feet, 5.5 inches")]),
    html.H2("Weight"),
    html.Ul(className= "specs-ul", children= [html.Li("113.5 pounds")]),
    html.H2("Elevator"),
    html.Ul(className= "specs-ul", children=[html.Li("GreyT Cascade Elevator, 3 Stage - (West Coast Products)")])
])
