"""hello and this code will need to have all of the important features like from
 guizero import App, Box, Text and use it to code resturants, check in, and 
 everything else that could be needed in a hotel, when you check in your name
 will be put into a list you could save the list as a txt.file and then split
 it back into a list when loaded and split into a list of one person and then 
 would be put into the new files list, """

from tkinter import messagebox, simpledialog, Tk

guests = dict()

while True:
    name = simpledialog.askstring(title="Hello welcome to joy hotels check in", prompt="What is your name?")
    value = simpledialog.askstring(title="Hello welcome to joy hotels check in", prompt="What room would you like?")
    nights = simpledialog.askstring(title="Hello welcome to joy hotels check in", prompt="how many nights are you staying?")

    