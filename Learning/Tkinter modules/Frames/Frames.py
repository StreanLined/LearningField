from tkinter import *
from PIL import ImageTk, Image


main = Tk()
main.title("Frame")

# Objects
frame = LabelFrame(main, text="Frame", padx=50, pady=50)
b = Button(frame, text="Button")
b2 = Button(frame, text="Exit", command=quit)
frame2 = LabelFrame(main, padx=20, pady=20)
b3 = Button(frame2, text="Quit", command=quit)


# Placement
frame.pack(padx=10, pady=10)
b.grid(row=0, column=0)
b2.grid(row=1, column=0)
frame2.pack(padx=20, pady=20)
b3.grid(row=0, column=0)

main.mainloop()
