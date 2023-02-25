from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title("Dropdown Menu")

def update():
    myLabel = Label(main, text=clicked.get())
    myLabel.pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

# Objects
menu_1 = OptionMenu(main, clicked, *options)
check_selection = Button(main, text="Do something", command=update)

# Placement
menu_1.pack()
check_selection.pack()

main.mainloop()
