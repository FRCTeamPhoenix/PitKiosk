#necessary imports
import dash
from dash import html
import dash_gif_component as gif

#setup page layout
layout =  html.Div ([
    html.H4(className = "touchscreen", children = "THIS IS TOUCHSCREEN!!!"),
    html.H1("Welcome to Team Phoenix"),
    html.P("Learn more about our robot and team by using our pit kiosk!"), 
    gif.GifPlayer(gif= 'assets/robot_rotating_gif.GIF', still= 'assets/robotgif_still.jpg'),
    html.Img(className= "home_img", src="/assets/robot_full_cad.png")
])





