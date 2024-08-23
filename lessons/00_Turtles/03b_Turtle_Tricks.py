"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle 
import random                         # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()    
tina.shape('circle')         
tina.speed(12)     
                                          # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.pencolor('red')
tina.pendown()
sides = 5
for i in range(sides):
    color = ['green', 'red', 'blue']
    
    tina.pencolor()
    tina.forward(100)
    tina.right(360/sides)

turtle.exitonclick()                    # Close the window when we click on it
