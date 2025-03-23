"""hello and this code will need to have all of the important features like from
 guizero import App, Box, Text and use it to code resturants, check in, and 
 everything else that could be needed in a hotel, when you check in your name
 will be put into a list you could save the list as a txt.file and then split
 it back into a list when loaded and split into a list of one person and then 
 would be put into the new files list, """

from tkinter import messagebox, simpledialog, Tk

guests = dict()
rooms = []

menu = dict()
menu["omllete"] = 3.50
menu["chips"] = 1.25
menu["pancakes"] = 12.50
menu["coffe"] = 4.00

def checkin():
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
def goto_reastraunt():
    messagebox.showinfo(title="...", message=" you see a cafe")
    messagebox.showinfo(title="welcome to sunberry beach cafe ", message=" what would you like")
    order = simpledialog.askstring(title="Menu", prompt="omellet -- 3.50, chips -- 1.25, pancakes -- 12.50, coffe -- 4.00")

    for menuitem in menu.keys():
        if order.find(menuitem)!=-1:
            cost = menu[menuitem] 
            messagebox.showinfo(title="your cost is", message=cost)


while True:
    choice = simpledialog.askstring(title="Hello welcome what do you want to do", prompt="checkin, checkout, goto_reastraunt")

    if choice == "checkin":
        checkin()

    elif choice == "goto_reastraunt":
        goto_reastraunt()

    elif choice == "checkout":
        Name = simpledialog.askinteger(title="Hello welcome to joy hotels check out", prompt="whats your name?")
        
