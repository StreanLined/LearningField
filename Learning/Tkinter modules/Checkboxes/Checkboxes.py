from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title("Frame")

var1 = StringVar()


def update():
    myLabel = Label(main, text=var1.get())
    myLabel.pack()


# Objects
checkbox_1 = Checkbutton(main, text="checkbox 1", variable=var1, onvalue="on", offvalue="off", command=update)
checkbox_1.deselect()
myLabel = Label(main, text="")

# Placement
checkbox_1.pack()
myLabel.pack()

main.mainloop()
