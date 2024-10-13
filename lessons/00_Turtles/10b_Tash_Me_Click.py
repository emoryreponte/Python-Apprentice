# Tash Me with a Click

import turtle
t = turtle.Turtle()

turtle.setup(width=600, height=600)                 
screen = turtle.Screen() 

def set_background_image(window, image_name):

    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

set_background_image(screen, "emoji2.png")

def set_turtle_image(turtle, image_name):

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

set_turtle_image(t, "moustache1.gif")

t.penup()

def screen_clicked(x, y):
    t.goto(x, y)

screen.onclick(screen_clicked)

turtle.done()  

# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'


