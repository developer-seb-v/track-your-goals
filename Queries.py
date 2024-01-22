import sqlite3
from datetime import datetime
from tkinter import *


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
