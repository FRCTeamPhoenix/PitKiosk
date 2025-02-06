#necessary imports
import dash
from dash import html
import dash_bootstrap_components as dbc


#setup page layout
layout =  html.Div ([
    html.H1("Subsystems"),
    html.Div("We've got a bunch of them."),
    html.H2("Drive"), 
    html.P(children="The drivetrain is a system of components that help the robot move around. It is the base of the robot and uses motors and wheels. We use swerve drive."),
    html.H2("Claw"),
    html.P(children="The claw intakes game pieces and helps hold them during transport. A motor causes the wheels in the claw to spin, and depending on the direction, it can either take in or push out pieces."),
    html.H2("Photon Vision"),
    html.P(children="This subsytem helps with vision-based target tracking, and provides like target distance, angle, and position. It is used to track AprilTags, which are on the field and help the robot align to targets."),
    html.H2("Elevator"),
    html.P(children="The elevator helps the robot to actually reach different heights for intaking and scoring game pieces. "),
#work in progress, needs to have more info
])
