#!/bin/python3

import sqlite3

def open_connection():
conn=sqlite3.connet("firstdb.db")
    cursor=conn.cursor()

name=input("what your name? ")
print(f"hello {name}")

open_connection()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS names(
                    id integer PRIMARY KEY AUTOINCREMENT,first_name TEXT, 
                                                         last_name TEXT
               )
""")
conn.commit()
conn.close()

