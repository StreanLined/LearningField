from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title("Image viewer")


def image_back(image_number):
    global image_window
    global back_button
    global forward_button
    image_window.grid_forget()
    image_window = Label(image=image_list[image_number-1])
    back_button = Button(main, text="<<", command=lambda: image_back(image_number-1))
    forward_button = Button(main, text=">>", command=lambda: image_forward(image_number+1))

    if image_number == 1:
        back_button = Button(main, text="<<", state=DISABLED)

    image_window.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(main, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def image_forward(image_number):
    global image_window
    global back_button
    global forward_button
    image_window.grid_forget()
    image_window = Label(image=image_list[image_number-1])
    back_button = Button(main, text="<<", command=lambda: image_back(image_number-1))
    forward_button = Button(main, text=">>", command=lambda: image_forward(image_number+1))

    if image_number == 8:
        forward_button = Button(main, text=">>", state=DISABLED) 

    image_window.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(main, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


i1 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/aoshin.png"))
i2 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/asol.png"))
i3 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/bard.png"))
i4 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/pyke.png"))
i5 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/shyvana.png"))
i6 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/soraka.png"))
i7 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/yasuo.png"))
i8 = ImageTk.PhotoImage(Image.open("C:/Python/Image viewer/images/zoe.png"))
image_list = [i1, i2, i3, i4, i5, i6, i7, i8]

# objects
image_window = Label(image=i1)
back_button = Button(main, text="<<", command=image_back, state=DISABLED)
exit_button = Button(main, text="Exit", command=main.quit)
forward_button = Button(main, text=">>", command=lambda: image_forward(2))
status = Label(main, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

# placement
image_window.grid(row=0, column=0, columnspan=3)
back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)



main.mainloop()
