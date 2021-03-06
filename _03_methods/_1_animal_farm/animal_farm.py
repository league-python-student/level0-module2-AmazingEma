from tkinter import simpledialog, Tk

from playsound import playsound
from PIL import Image


def moo():
    im = Image.open("cow.jpg")
    im.show()
#    playsound('moo.wav')

def quack():
    im = Image.open("duck.jpg")
    im.show()
#    playsound('quack.wav')

def woof():
    im = Image.open("dog.jpg")
    im.show()
#    playsound('woof.wav')

def meow():
    im = Image.open("cat.jpg")
    im.show()
 #   playsound('meow.wav')

def llama_scream():
    im = Image.open("llama.jpg")
    im.show()
#    playsound('llama.wav')

def animals():
    window = Tk()
    window.withdraw()

    # TODO 1.Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.
    for i in range(10000000000):
        z = simpledialog.askstring("None","what animal would you like?")
    # TODO 2. Make it so that the user can keep entering new animals.
        if z == "cow":
            moo()
        elif z == "duck":
            quack()
        elif z == "dog":
            woof()
        elif z == "cat":
            meow()
        elif z == "llama":
            llama_scream()
        else:
            print("unknown animal")

if __name__ == '__main__':
    animals()
