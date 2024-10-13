
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

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

#def set_turtle_image(turtle, image_name):

    #from pathlib import Path
    #image_dir = Path(__file__).parent / "images"
    #image_path = str(image_dir / image_name)

    #screen = turtle.getscreen()
    #screen.addshape(image_path)
    #turtle.shape(image_path)

#set_turtle_image(t, "moustache1.gif")

t.penup()
t.shape('turtle')
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def screen_clicked(x, y):
    t.goto(x, y)

screen.onclick(screen_clicked)

def turtle_clicked(t, x, y):

    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        t.tilt(20) # Tilt the turtle 20 degrees

t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))



turtle.done() 

