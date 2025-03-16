"""hello and this code will need to have all of the important features like from
 guizero import App, Box, Text and use it to code resturants, check in, and 
 everything else that could be needed in a hotel, when you check in your name
 will be put into a list you could save the list as a txt.file and then split
 it back into a list when loaded and split into a list of one person and then 
 would be put into the new files list, """

from tkinter import messagebox, simpledialog, Tk

guests = dict()
rooms = []

while True:
    choice = simpledialog.askstring(title="Hello welcome what do you want to do", prompt="checkin, checkout, goto_restraunt")
    if choice == "checkin":
        name = simpledialog.askstring(title="Hello welcome to joy hotels check in", prompt="What is your name?")
        validroom = False
        while validroom == False:
            value = simpledialog.askinteger(title="Hello welcome to joy hotels check in", prompt="What room would you like?")
            validroom = True
            for room in rooms:
                if room == value:
                    messagebox.showinfo(title="please pick another room", message=name)
                    validroom = False
        nights = simpledialog.askinteger(title="Hello welcome to joy hotels check in", prompt="how many nights are you staying?")

        guests[name] = (value, nights)
        rooms.append(value)
        print(guests)
        print(rooms)


    elif choice == "goto_restraunt":
        messagebox.showinfo(title="its time to leave ", message=name)
        messagebox.showinfo(title="...", message=" you see a cafe")
        messagebox.showinfo(title="welcome to sunberry beach cafe ", message=name+" what would you like")
        
