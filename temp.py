import sqlite3
import os
con = sqlite3.connect('log.db')
cur = con.cursor()
cur.execute('''CREATE TABLE logone
         (message text, number integer, datetime timestamp)''')
# cur.execute('''INSERT INTO logone (message, number, datetime )
# VALUES('hello3',1323,datetime('now', 'localtime'))''')
# cur.execute('''INSERT INTO logone (message, number, datetime )
#  VALUES('hello3',123,datetime('now', 'localtime'))''')
# cur.execute('''INSERT INTO logone (message, number, datetime )
#  VALUES('hello3',2345,datetime('now', 'localtime'))''')
# cur.execute('''INSERT INTO logone (message, number, datetime )
#  VALUES('hello3',234523,datetime('now', 'localtime'))''')
# cur.execute('''INSERT INTO logone (message, number, datetime )
#  VALUES('hello3',2324134,datetime('now', 'localtime'))''')
con.commit()
sqlite_select_query = """SELECT MAX(number) from logone"""
cur.execute(sqlite_select_query)
records = cur.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
print(records[0][0])