from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

main = Tk()
main.title("Files")
main.geometry("400x400")


def update():
    main.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# Objects
vertical = Scale(main, from_=0, to=400)
horizontal = Scale(main, from_=0, to=400, orient=HORIZONTAL)

myLabel = Label(main, text="")
updatebutton = Button(main, text="Update", command=update)

# Placement
vertical.pack()
horizontal.pack()
myLabel.pack()
updatebutton.pack()


main.mainloop()
