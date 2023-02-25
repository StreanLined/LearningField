from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

main = Tk()
main.title("Message_box")

# variants
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    #messagebox.showinfo("This is a popup", "Popup2")
    response = messagebox.askyesno("askyesno", "?")
    #Label(main, text=response).pack()
    if response == 1:
        Label(main, text="You clicked yes").pack()
    else:
        Label(main, text=":(").pack()


# Objects
myButton = Button(main, text="Popup button", command=popup).pack()

# Placement


main.mainloop()
