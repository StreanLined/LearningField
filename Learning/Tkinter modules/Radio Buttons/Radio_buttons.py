from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title("Radio_buttons")

A = IntVar()
A.set(2)

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
    ("Tuna", "Tuna"),
]

pizza = StringVar()
pizza.set(" ")

for topping, sort in MODES:
    Radiobutton(main, text=topping, variable=pizza, value=sort).pack(anchor=W)

def update(value):
    mylabel = Label(main, text=value)
    mylabel.pack()



# Objects
myButton = Button(main, text="Update", command=lambda: update(pizza.get())).pack()


# Placement


main.mainloop()
