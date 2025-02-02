from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()



# 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 10)

# 3. Code a for loop to run steps 4-10, 10 times
def ask_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid number!")


for i in range(4):
    p = ask_integer("guss the number ")

    if p == random_num:
        print("you win")
        sys.exit(0)
    elif p < random_num:
        print("guess to low")
    elif p > random_num:
        print("guess to high")

print ("you lose the number was " + str(random_num))
    # 5. If the guess is correct
        # 6. Win. Use 'sys.exit(0)' to end the program

    # 7. if the guess is high
        # 8. Tell them it's too high
    # 9. Else if the guess is low
        # 10. Tell them it's too low

#11. Outside of the loop, tell the user they lost

window.mainloop()
