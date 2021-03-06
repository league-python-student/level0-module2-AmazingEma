import random
from tkinter import messagebox, Tk


for i in range(10):
    if __name__ == '__main__':
        window = Tk()
        window.withdraw()

        random_number = random.randint(1, 5)

        print(random_number)
    # TODO 1) Use each value of random_number to give the user a random compliment
    if random_number == 5:
        print("you are very friendly")
    elif random_number == 4:
        print("you are awesome")
    elif random_number == 3:
        print("have a nice day")
    elif random_number == 2:
        print("i wish i were you")
    else:
        print('insert you fav compliment here')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
