#necessary imports
import dash
from dash import html
import dash_bootstrap_components as dbc


#setup page layout
layout =  html.Div ([
    html.H1("Subsystems"),
    html.Div("We've got a bunch of them."),
    html.H2("Drive"), 
    html.Div(id='drive', children="Drive Info"),
    html.H2("Claw"),
    html.Div(id='claw', children="Claw Info"),
    html.H2("Photon"),
    html.Div(id='photon', children="Photon Info"),
    html.H2("Elevator"),
    html.Div(id='elevator', children="Elevator Info"),
#work in progress, needs to have more info and be aligned differently
])
