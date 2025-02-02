#necessary imports
import dash
from dash import html
import dash_bootstrap_components as dbc


#setup page layout
layout =  html.Div ([
    html.H1("Subsystems"),
    html.Div("We've got a bunch of them."),
    html.H2("Drive"), 
    html.P(children="Drive Info"),
    html.H2("Claw"),
    html.P(children="Claw Info"),
    html.H2("Photon"),
    html.P(children="Photon Info"),
    html.H2("Elevator"),
    html.P(children="Elevator Info"),
#work in progress, needs to have more info
])
