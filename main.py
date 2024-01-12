# tkinter gui app
import tkinter
from tkinter import *

from tkcalendar import DateEntry

from query import *

# tkinter

# db
# create db
conn = sqlite3.connect('database.db')

# create cursor
c = conn.cursor()

# # create table
# c.execute(
#    """
#    CREATE TABLE IF NOT EXISTS goal (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    name VARCHAR(255) NOT NULL,
#    description VARCHAR(255) NOT NULL,
#    date_created DATETIME NOT NULL
#    )
#    """
# )


# commit changes
conn.commit()

# close connection
conn.close()


# queries
def insert(name, description, date_created):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""
       INSERT INTO goal (name, description, date_created)
       VALUES(?,?,?)
      """, (name, description, date_created))
    conn.commit()
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

# goal name entry widget
goal_name = Entry(main, width=30)
goal_name.pack(side=TOP)
goal_name_input = goal_name.get()

desc_label = tkinter.Label(text="Goal Description", font="Arial")
desc_label.pack(side=TOP)

# goal description entry widget
goal_description = Entry(main, width=30)
goal_description.pack(side=TOP)
goal_description_input = goal_description.get()

due_date_label = tkinter.Label(text="Due Date", font="Arial")
due_date_label.pack(side=TOP)

# due date picker widget
date_picker = DateEntry(main, width=10)
date_picker.pack(side=TOP)
date_picker_input = date_picker.get_date()

# button with sql insert method as command
add_button = Button(main, text="Add Goal", command=lambda:  insert("lose weight", "lose 10 lbs", "06-01-2024"))
add_button.pack(side=TOP)

main.mainloop()
