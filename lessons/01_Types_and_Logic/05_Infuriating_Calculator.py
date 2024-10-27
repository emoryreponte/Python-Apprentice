"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window; we just want to see pop ups

a = simpledialog.askinteger(title="Hello", prompt="please enter number 1") # Ask the user for the first number   

b = simpledialog.askinteger(title="Hello", prompt="please enter number 2") # Ask the user for the second number

c = simpledialog.askstring(title="Hello", prompt="please enter opperation")# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if c.lower() == "addition":
   messagebox.showinfo("its",str(a + b))

elif c.lower() == "subtraction":
   messagebox.showinfo("its",str(a - b))

elif c.lower() == "multiplication":
   messagebox.showinfo("its",str(a * b))

elif c.lower() == "division":
   messagebox.showinfo("its",str(a / b))

else:
   messagebox.showerror()

window.mainloop() # Keep the window open
