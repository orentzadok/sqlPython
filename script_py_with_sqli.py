#!/bin/python3

import sqlite3

conn=sqlite3.connect("firstdb.db")
cursor=conn.cursor()

name=input("what your name? ")
print(f"hello {name}")


cursor.execute("""
               CREATE TABLE IF NOT EXISTS names(
                    id integer PRIMARY KEY AUTOINCREMENT,first_name TEXT, 
                                                         last_name TEXT
               )
""")
cursor.execute("INSERT INTO names (first_name, last_name) VALUES(?,?)", (name,name))
conn.commit()
cursor.execute("SELECT * FROM names")
rows=cursor.fetchall()
for row in rows:
	print(row)

conn.close


