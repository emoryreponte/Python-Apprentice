"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox, simpledialog, Tk

# TODO)
turt = turtle
turt.speed(2)
turt.screensize(500, 500)

def square(turt):
    for i in range(4):
        turt.forward(100)
        turt.right(90)

def triangle(turt):
    for i in range(3):
        turt.forward(100)
        turt.right(120)

def sphere(turt):
    turt.circle(100, steps=50)

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

shape = simpledialog.askstring(title="Hello", prompt="please enter a shape")

if shape == "square":
    square(turt)

if shape == "triangle":
    triangle(turt)

if shape == "circle":
    sphere(turt)

turtle.exitonclick()