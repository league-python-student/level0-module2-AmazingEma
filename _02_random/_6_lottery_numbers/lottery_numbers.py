import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
for i in range(6):
    r = random.randint(0,9)
    # TODO 2) Display the selected numbers to the user in a pop-up

    messagebox.showinfo("Your lottery numbers are...", r)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
