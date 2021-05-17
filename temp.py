import sqlite3
import os
con = sqlite3.connect('log.db')
cur = con.cursor()
# cur.execute('''CREATE TABLE logone
#         (message text, number integer, datetime timestamp)''')
cur.execute('''INSERT INTO logone (message, number, datetime )
VALUES('hello',123,datetime('now', 'localtime'))''')
sqlite_select_query = """SELECT * from logone"""
cur.execute(sqlite_select_query)
records = cur.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
for row in records:
    print(row)