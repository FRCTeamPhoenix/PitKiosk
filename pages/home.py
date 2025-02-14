#necessary imports
import dash
from dash import html

#setup page layout
layout =  html.Div ([
    html.H1("Welcome to Team Phoenix"),
    html.P("Learn more about our robot and team by using our pit kiosk!"), 
    html.Img(className= "home-img", src="/assets/robot_side_cad.png")
])

