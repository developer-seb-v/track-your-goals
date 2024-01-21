import sqlite3
from datetime import datetime


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
