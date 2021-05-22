import os
import sys
import sqlite3
import datetime

class LogUtils:

    @staticmethod
    def msgAndNumCheck(msg, num):
        """
        Checks Commit Message & Commit Number are in the correct format 
        
        @param msg: Commit Message
        @param num: Commit Number

        @return Commit Message & Commit Number are in the correct format
                else returns False

        """
        return(isinstance(msg, str) and isinstance(num,int)
            and len(msg) > 0 and len(msg) < 128
            and int(num) > 0
            and msg is not None and num is not None
            )
    
    @staticmethod
    def updateLogfile(cm_dir,msg,num):
        """
        Updates log file with Commit Message, Commit Number and Datetime
        
        @param cm_dir : Path to the Commit Man Directory 
        @param msg: Commit Message
        @param num: Commit Number
 
        """
        if msgAndNumCheck(msg, num):
            if os.path.exists(os.path.join(cm_dir,'log.db')):
                    try:
                        con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                        cur = con.cursor()
                        sql = '''INSERT INTO log (message, number, datetime ) VALUES(?,?,datetime('now', 'localtime'))'''
                        cur.execute(sql,[msg,num,])
                        con.commit()
                        con.close()
                    except Exception as e:
                        raise Exception(f'SQL database could not be updated : {e}')
            else:
                raise Exception('Cannot find log file')
        else:
            raise Exception('Check commit msg')
    
    @staticmethod
    def genrateLogfile(dir_path,test=False):
        if not test:
            with open(os.path.join(os.path.join(dir_path, '.cm'),'log.db'), 'w') as f:
                pass
            try:
                con = sqlite3.connect(os.path.join(os.path.join(dir_path, '.cm'),'log.db'))
                cur = con.cursor()
                cur.execute('''CREATE TABLE log (message text, number integer, datetime timestamp)''')
                cur.execute('''INSERT INTO log (message, number, datetime ) VALUES ('Created repo',0,datetime('now', 'localtime'))''')
                con.commit()
                con.close()
            except Exception as e:
                print(f"Failed to Create log file due to : {e}")
            finally:
                if con:
                    con.close()
        else:
            try:
                con = sqlite3.connect(os.path.join(os.path.join(dir_path, '.cm'),'log.db'))
                cur = con.cursor()
                cur.execute('''INSERT INTO log (message, number, datetime ) VALUES ('Created repo',-1,datetime('now', 'localtime'))''')
                cur.execute('''DELETE FROM log WHERE number=-1''')
                con.commit()
                con.close()
            except Exception:
                return False