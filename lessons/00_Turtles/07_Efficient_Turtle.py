
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina


tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
tina.pendown()
tina.pencolor('red')

def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides

    for i in range(sides):                 # Loop through the number of sides
        tina.forward(100)                      # Move tina forward by the forward distance
        tina.left(angle)                            # Turn tina left by the left turn

def draw_things():
    tina.penup()
    tina.goto(150, 150)
    tina.pendown()
    draw_polygon(4)
    tina.penup()
    tina.goto(0, 0)
    tina.pendown()
    draw_polygon(6)
    tina.penup()
    tina.goto(-150, -150)
    tina.pendown()
    draw_polygon(5)

draw_things()

turtle.exitonclick()                     # Close the window when we click on it
