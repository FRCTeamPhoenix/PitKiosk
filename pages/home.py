#necessary imports
import dash
from dash import html
import dash_gif_component as gif

#setup page layout
layout =  html.Div ([
    html.H1("Welcome to Team Phoenix"),
    html.P("Learn more about our robot and team by using our pit kiosk!"), 
    gif.GifPlayer(gif= 'assets/robot_rotating_gif.GIF', still= 'assets/robotgif_still.jpg')
    #html.Img(className= "home-img", src="/assets/robot_side_cad.png")
])


