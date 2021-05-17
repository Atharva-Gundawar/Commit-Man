import sqlite3
import os
import datetime
with open('log.db', 'w') as f:
    pass
con = sqlite3.connect('log.db')
cur = con.cursor()
cur.execute('''CREATE TABLE log
        (message text, number integer, datetime timestamp) ''')
cur.execute(f"INSERT INTO stocks VALUES ('textttt',5,{datetime.datetime.now()})")
