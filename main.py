# tkinter gui app
import tkinter
from tkinter import *
import ttkbootstrap
import sqlite3
from datetime import datetime
from ttkbootstrap.dialogs import Messagebox


# create table if it hasn't been created

def create_table():
    # create db
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
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
    conn.commit()
    conn.close()


# insert a goal into the db
def insert(n, descr, created: datetime):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute("""
               INSERT INTO goal (name, description, date_created)
               VALUES(?,?,?)
              """, (n, descr, created))
        conn.commit()
        Messagebox.ok("Your goal has been added", "Add Goal", alert=True, parent=main)
    except sqlite3.Error as error:
        print(error)
    conn.close()


# grab goals and display in tkinter labels
def get_goals():
    nw = Tk()
    nw.title("Goal Tracker")
    nw.geometry('500x650')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM goal")
        r = c.fetchall()

        num = 2
        for i in r:
            name = Label(nw, text=i[0], font="time 12 bold", fg="blue", padx=10, pady=10)
            name.grid(row=num, column=0)
            descr = Label(nw, text=i[1], font="time 12 bold", padx=10, pady=10)
            descr.grid(row=num, column=1)
            date = Label(nw, text=i[2], font="time 12 bold", padx=10, pady=10)
            date.grid(row=num, column=2)

            num = num + 1

        conn.commit()
    except sqlite3.Error as error:
        print(error)
        conn.close()


# tkinter

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

view_goals_btn = (ttkbootstrap.Button(main, text="View Goals", command=lambda: get_goals()))
view_goals_btn.pack(side=TOP, padx=20, pady=20)

main.mainloop()
