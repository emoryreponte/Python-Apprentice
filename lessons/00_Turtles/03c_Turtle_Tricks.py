"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle    
import random                       # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
t = turtle.Turtle()                  # Create a turtle named tina
t.speed(2)
# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
t.goto(-100, 0)
t.pencolor('red')
t.pensize(10)

t.pendown()

sides = 3  
t.begin_fill()
t.fillcolor('black')
for i in range(sides):
    c = ['red', 'blue', 'green']

    t.pencolor(c[i])
    t.forward(100)
    t.right(360/sides)
t.end_fill()

t.penup()
t.goto (100, 0)
t.pendown()
sides = 5
t.begin_fill()
t.fillcolor('black')
for i in range(sides):
    c = ['red', 'blue', 'green', 'pink', 'purple']

    t.pencolor(c[i])
    t.forward(100)
    t.right(360/sides)
t.end_fill()

turtle.exitonclick()                    # Close the window when we click on it
