from tkinter import *
from PIL import ImageTk, Image
import sqlite3

main = Tk()
main.title("Database")
main.geometry("340x600")


# Database


# Create a database or connect to one
conn = sqlite3.connect('address_book.db')


# Create cursor
c = conn.cursor()


# Create table
# c.execute("""CREATE TABLE addresses (
#        first_name text,
#        last_name text,
#        address text,
#        city text,
#        zipcode integer
#        )""")

# Create submit function for DB
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'zipcode': zipcode.get()
            }
              )
    conn.commit()
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid=" + delete_entry.get())
    conn.commit()
    conn.close()


# Query function
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(main, text=print_records)
    query_label.grid(row=20, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Create text boxes
f_name = Entry(main, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(main, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(main, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(main, width=30)
city.grid(row=3, column=1, padx=20)

zipcode = Entry(main, width=30)
zipcode.grid(row=4, column=1, padx=20)

# Create text box labels
f_name_label = Label(main, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(main, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(main, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(main, text="City")
city_label.grid(row=3, column=0)

zipcode_label = Label(main, text="ZIP Code")
zipcode_label.grid(row=4, column=0)

# Create submit button
submit_btn = Button(main, text="Add Record to DB", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Delete Button
delete_button = Button(main, text="Delete Records", command=delete)
delete_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=112)

# Query Button
query_button = Button(main, text="Show Records", command=query)
query_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=112)
delete_entry = Entry(main, width=30)
delete_entry.grid(row=7, column=1)
delete_entry_label = Label(main, text="ID")
delete_entry_label.grid(row=7, column=0)

# Commit connection
conn.commit()

# Close connection
conn.close()

# Objects


# Placement


main.mainloop()
