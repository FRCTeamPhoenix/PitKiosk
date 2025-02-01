from dash import Dash, html  #imports

app = Dash() #initialize

app.layout = [html.Div(children='Hello World')] # components that will be displayed in the web browser given as list; could be Dash component
#single component was added to the list: an html.Div. The Div has a few properties, such as children, which we use to add text content to the page: "Hello World".


# Run the app
if __name__ == '__main__':
    app.run(debug=True) #runs the app, almost always same for all dash apps