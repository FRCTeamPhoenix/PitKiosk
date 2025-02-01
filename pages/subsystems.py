#necessary imports
import dash
from dash import html
import dash_bootstrap_components as dbc


#setup page layout
layout =  html.Div ([
    html.H1("Subsystems"),
    html.Div("We've got a bunch of them."),
    html.H2("Drive"), 
    html.Div("Information about drive"),
    html.H2("Claw"),
    html.Div("Information about claw"),
    html.H2("Photon"),
    html.Div("Information about photon"),
    html.H2("Elevator"),
    html.Div("Information about elevator"),
#work in progress, needs to have more info and be aligned differently
])
