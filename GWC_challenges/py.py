
from turtle import *
import math

# Name your Turtle.
banana = Turtle()

# Set Up your screen and starting position.
banana.penup()

#setting position to draw the square
setup(500,300)
x_pos = -250
y_pos = -150
banana.setposition(x_pos, y_pos)

#picking a color for shapes
color=input("What color would you like to make your shapes? Pick blue or red:")
if color=="red":
    banana.pencolor("red")
elif color=="blue":
    banana.pencolor("blue")
else:
    print("Please pick a color")
banana.pendown()

#code for drawing the square:
for i in range (4):
    banana.forward(50)
    banana.left(90)

#resetting the coordinates so it can draw the triangle
banana.penup()
x_pos = 250
y_pos = 150
banana.setposition(x_pos, y_pos)

#code for drawing the triangle
banana.pendown()
def draw_triangle ():
    for i in range (3):
        banana.forward(50)
        banana.left(120)
draw_triangle()

# Close window on click.
exitonclick()
