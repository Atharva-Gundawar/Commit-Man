import sqlite3

con = sqlite3.connect('.cm/log.db')
cur = con.cursor()
# sqlite_select_query = """SELECT name FROM sqlite_master"""
# cur.execute('''CREATE TABLE log(message text, number integer, datetime timestamp)''')
# cur.execute('''INSERT INTO log (message, number, datetime )VALUES('Created repo',0,datetime('now', 'localtime'))''')
sqlite_select_query = """SELECT * from log"""
cur.execute(sqlite_select_query)
v_num = cur.fetchall()
print(v_num)
con.close()