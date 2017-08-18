from turtle import *
import math

# Name your Turtle
t= Turtle()

# Set Up your screen and starting position.
#setting position to draw the square
setup(500,300)
x_pos = 0
y_pos = 0
pendown()
t.setposition(x_pos, y_pos)

#picking a color for shapes and picking the number of sides for a shape
inputtext=input("How many number of sides would you like? Choose a number greater than three:")
sides=int(inputtext)

# colortext=input("What color would you like to make your shapes? Pick blue or red:")
# color=colortext

#code for drawing the shapes
def draw(sides):
	for i in range(sides):
		pendown()
		# pencolor(color)
		forward(50)
		left(360/sides)
draw(sides)


# Close window on click.
exitonclick()
