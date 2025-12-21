#!/bin/python3

import sqlite3

conn=sqlite3.connect("firstdb.db")
cursor=conn.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS names(
                    id integer PRIMARY KEY AUTOINCREMENT,first_name TEXT, 
                                                         last_name TEXT
               )
""")
name=""
choice=input("if you want to delete the table press 1 ")
if choice=="1":
    cursor.execute("DELETE FROM names")
    conn.commit()
else:
    name = input("what your name? ")
    while name!="stop":

        print(f"hello {name}")

        cursor.execute("INSERT INTO names (first_name, last_name) VALUES(?,?)", (name,name))
        conn.commit()
        cursor.execute("SELECT first_name,last_name FROM names")
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        name = input("what your name? ")

conn.close


