# tkinter gui app
import tkinter
from tkinter import *
from tkcalendar import DateEntry

main = Tk()
main.title("Goal Tracker")
main.geometry('600x450+500+250')

top_frame = Frame(main)
top_frame.pack(side=TOP, fill='both')

label = tkinter.Label(text="Goal Name", font="Arial")
label.pack(side=TOP)

goal_name = Text(main, width=30, height=2)
goal_name.pack(side=TOP)

due_date_label = tkinter.Label(text="Due Date", font="Arial")
due_date_label.pack(side=TOP)
date_picker = DateEntry(main, width=10)
date_picker.pack(side=TOP)

add_button = Button(main, text="Add")
add_button.pack(side=TOP)

main.mainloop()
