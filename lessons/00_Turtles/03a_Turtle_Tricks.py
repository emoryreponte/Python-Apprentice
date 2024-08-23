"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
import random
turtle.setup (width=600, height=600)    # Set the size of the window
                                        # Create a turtle named tina
tina = turtle.Turtle()   
tina.shape('circle')         
tina.speed(12)     

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
# Your code here

tina.pencolor('red')
tina.pendown()
for i in range(3):
    tina.pencolor({random.randint(0, 255)})
    tina.forward(100)
    tina.right()

turtle.exitonclick()                    # Close the window when we click on it
