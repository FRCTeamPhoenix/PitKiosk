#necessary imports
import dash
from dash import html, dcc


#setup page layout
layout =  html.Div ([
    html.H1("About Us"),
    html.Ul(id = "about_list", children= [html.Li("Founded in 2007"), 
                                          html.Li("4-H Robotics Club"),
                                          html.Li("Based in Nashua NH"),
                                          html.Li("Members from high schools across southern New Hampshire"), 
                                          html.Li("52 members, 23 mentors"),
                                          ])

])