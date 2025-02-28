#necessary imports
import dash
from dash import html
import dash_bootstrap_components as dbc


#setup page layout
layout =  html.Div ([
    html.H1("Subsystems"),
    html.H2("Drive"), 
    html.P(className= "subsystem-p", children="The drivetrain is a system of components that help the robot move around. It is the base of the robot and uses motors and wheels. We use swerve drive."),
    html.Img(className= "subsystem_img", src="/assets/drive_cad.png"),
    html.H2("Claw/Wrist"),
    html.P(className= "subsystem-p", children="The claw intakes game pieces and helps hold them during transport. A motor causes the wheels in the claw to spin, and depending on the direction, it can either take in or push out pieces. The wrist mechanism uses a motor and allows the claw to tilt to set angles for intake and scoring. ", id = "subsystem-p"),
    html.Img(className= "subsystem_img", src="/assets/claw_cad.png"),
    html.H2("Photon Vision"),
    html.P(children="This subsytem helps with vision-based target tracking, and provides like target distance, angle, and position. It is used to track AprilTags, which are on the field and help the robot align to targets."),
    html.H2("Elevator"),
    html.P(className= "subsystem-p", children="""The elevator helps the robot to reach different heights for intaking and scoring game pieces. It uses two motors and has different setpoints that correspond to the levels on the reef. """),
    html.Img(className= "subsystem_img", src="/assets/elevator_cad.png"),
    html.H2("Climber"),
    html.P(className= "subsystem-p", children="The climber is the mechanism that helps the robot complete endgame. It grabs the cage and helps the robot get off the ground. This year, the robot will be doing a deep climb."),
    html.Img(className= "subsystem_img", src="/assets/climber_cad.png")
])
