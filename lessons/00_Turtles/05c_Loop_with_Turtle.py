
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here

import turtle
t = turtle.Turtle()


t.goto (0, 0)
t.pendown()
t.pensize(10)
sides = 5
for i in range(sides):
    c = ['red', 'blue', 'green', 'pink', 'purple']

    t.pencolor(c[i])
    t.forward(100)
    t.right(360/sides)

turtle.exitonclick()
