#necessary imports
import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc 
from dash.exceptions import PreventUpdate
import os 

#import pages
from pages import home, about, subsystems, specs, matches

#create app
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

#define navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                ["Home", html.Img(src="/assets/home.png", style={'margin-left': '10px'})], 
                href="/", 
                id='home_button'
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                ["About", html.Img(src="/assets/about.png", style={'margin-left': '10px'})], 
                href="/about", 
                id='about_button'
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                ["Subsystems", html.Img(src="/assets/subsystems.png", style={'margin-left': '10px'})], 
                href="/subsystems", 
                id='subsystems_button'
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                ["Specifications", html.Img(src="/assets/specs.png", style={'margin-left': '10px'})], 
                href="/specs", 
                id='specs_button'
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                ["Match Information", html.Img(src="/assets/matches.png", style={'margin-left': '10px'})], 
                href="/matches", 
                id='matches_button'
            )
        )
    ],
    style= {'background-color': "#d9534f"},
    brand= dbc.Col(html.Img(src="/assets/WhiteRedBack.PNG", height= "95px")), 
    brand_href="/",
    color= '',
    dark=True, 
    id= 'navigation'
)

#Define app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,  #Navbar at the top
    html.Div(id='page-content')  #changes based on page
])

#routing pages
@app.callback(
    Output(component_id='page-content', component_property='children'),  #updating the 'children' of 'page-content'
    [Input(component_id='url', component_property='pathname')]  #checking for changes to the URL path
)

#logic for changing to pages
def display(pathname):
    if pathname == '/about':
        return about.layout
    elif pathname == '/subsystems':
        return subsystems.layout
    elif pathname == '/specs':
        return specs.layout
    elif pathname == '/matches':
        pass
        return matches.layout
    else:
        return home.layout

#actually runs the app
if __name__ == '__main__':
    app.run(debug=True)