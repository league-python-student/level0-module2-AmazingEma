import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
simpledialog.askstring("None", "ask your question for the mystics to answer")
    # Make a variable and initialize it to a random number between 0 and 3
    # If the random number is 0
num = random.randint(0,3)
        # tell the user "Yes"
if num == 0:
    messagebox.showinfo("None","the mystics say... YES")
    # If the random number is 1
elif num == 1:
    messagebox.showinfo("None", "the mystics say... NOOOO")
        # tell the user "No"
elif num == 2:
    messagebox.showinfo("None","the mystics say... to ask google")
    # If the random number is 2
else:
    messagebox.showinfo('None', "the mystics say... that you should find our yourself")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
