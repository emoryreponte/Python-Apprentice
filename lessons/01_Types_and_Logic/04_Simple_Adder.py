"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window; we just want to see pop ups

a = simpledialog.askinteger(title="Hello", prompt="please enter number 1") # Ask the user for the first number   

b = simpledialog.askinteger(title="Hello", prompt="please enter number 2")

messagebox.showinfo("its",str(a + b))# Display the sum of the two numbers 

window.mainloop() # Keep the window open
