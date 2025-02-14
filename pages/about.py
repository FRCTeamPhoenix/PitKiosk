#necessary imports
import dash
from dash import html, dcc


#setup page layout
layout =  html.Div ([
    html.H1("About Us"),
    html.P( className = "about-p", children= "Founded in 2007"),
    html.P( className = "about-p", children= "4-H Robotics Club"),
    html.P( className = "about-p", children= "Based in Nashua NH7"),
    html.P( className = "about-p", children= "Members from high schools across southern New Hampshire"),
    html.P( className = "about-p", children= "52 members, 23 mentors")
])