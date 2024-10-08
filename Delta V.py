import turtle
import math

# Renames the turtle to shorten code
bms = turtle.Turtle()
# Renames screen settings to shorten code
screen = turtle.Screen()

# Sets screensize to 50% Width and 50% Height of current screen.
# "None,None" centers the window on the screen's X axis and Y axis
screen.setup(.5,.5,None,None)
# Sets the window's title
screen.title("Tsiolkovsky Rocket Equation")
# Set's the screen's background color
screen.bgcolor("navy")
# Hides pen tip, essentially
bms.hideturtle()
# Sets pen color to blue
bms.pencolor("white")
# Sets pen tip size (width in pixels)
bms.pensize(13)

# DRAWING THE TRIANGLE
# Picks up the pen tip
bms.penup()
# Moves pen to a specific X,Y coordinate
bms.goto(-100,0)
# Put down the pen tip
bms.pendown()
# Moves pen forward by 90 pixels
bms.forward(90)
# Turns pen left 120 degrees
bms.left(120)
# Moves pen forward by 90 pixels
bms.forward(90)
# Turns pen left 120 degrees
bms.left(120)
# Moves pen forward by 90 pixels
bms.forward(90)
# Picks up the pen tip
bms.penup()

# DRAWING THE V
# Moves pen to a specific X,Y coordinate
bms.goto(0,80)
# Puts pen tip down
bms.pendown()
# Turns pen left 60 degrees
bms.left(60)
# Moves pen forward by 90 pixels
bms.forward(90)
# Turns pen left 125 degrees
bms.left(125)
# Moves pen forward by 90 pixels
bms.forward(90)
# Picks up the pen tip
bms.penup()
# Moves pen to a specific X,Y coordinate
bms.goto(0,80)
# Puts down the pen tip
bms.pendown()
# Turns pen left 80 degrees
bms.left(80)
# Draws the curly part of the V
for i in range(16):
    bms.forward(math.sqrt(i)*0.75)
    bms.left(i%10000000)

# Closes the window upon clicking
turtle.exitonclick()

