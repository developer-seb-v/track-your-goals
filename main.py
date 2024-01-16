# tkinter gui app
import sqlite3
import tkinter
from datetime import datetime
from tkinter import *
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap

# tkinter


# create db
conn = sqlite3.connect('database.db')

# create cursor
c = conn.cursor()

# create table
c.execute(
    """
   CREATE TABLE IF NOT EXISTS goal (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name VARCHAR(255) NOT NULL,
   description VARCHAR(255) NOT NULL,
   date_created DATETIME NOT NULL
   )
   """
)

# commit changes
conn.commit()

# close connection
conn.close()

# window properties
main = Tk()
main.title("Goal Tracker")
main.geometry('600x450+500+250')
top_frame = Frame(main)
top_frame.pack(side=TOP, fill='both')

# widgets
label = tkinter.Label(text="Goal Name", font="Arial")
label.pack(side=TOP)

name = StringVar()
desc = StringVar()


# queries
def insert(n, descr, created: datetime):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute("""
           INSERT INTO goal (name, description, date_created)
           VALUES(?,?,?)
          """, (n, descr, created))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    conn.close()
    mb = Messagebox.ok("Your goal has been added!", "Goals", parent=top_frame)
    goal_name.delete(0, 'end')
    goal_description.delete(0, 'end')
    goal_name.focus()


# goal name entry widget
goal_name = Entry(main, textvariable=name, width=30)
goal_name.pack(side=TOP)

desc_label = tkinter.Label(text="Goal Description", font="Arial")
desc_label.pack(side=TOP)

# goal description entry widget
goal_description = Entry(main, textvariable=desc, width=30)
goal_description.pack(side=TOP)

due_date_label = tkinter.Label(text="Due Date", font="Arial")
due_date_label.pack(side=TOP)

# due date picker widget
date_picker = ttkbootstrap.DateEntry(main, width=12)
date_picker.pack(side=TOP, padx=20, pady=20)
the_date = date_picker.entry.get()


# button with sql insert method as command
add_button = (ttkbootstrap.Button
              (main, text="Add Goal", command=lambda: insert(
               name.get(),
               desc.get(),
               date_picker.entry.get())))
add_button.pack(side=TOP, padx=20, pady=45)

main.mainloop()
