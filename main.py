# tkinter gui app
import tkinter
from tkinter import *
import ttkbootstrap
import Queries


# create table if it hasn't been created
Queries.create_table()

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
              (main, text="Add Goal", command=lambda: Queries.insert(
               name.get(),
               desc.get(),
               date_picker.entry.get())))
add_button.pack(side=TOP, padx=20, pady=45)

main.mainloop()
