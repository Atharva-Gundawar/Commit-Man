import datetime
import sqlite3
import sys
import os

class LogUtils:
    """
    LogUtils class contains all the functions
    required to handle the Log file.
    
    @functions
    msgAndNumCheck => Validates Message and number.
    updateLogfile  => Updates log file with Commit Message and Commit Number.
    genrateLogfile => Genrates and tests Logfile.
    display_log    => Displays logfile. 
    """

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
        if LogUtils.msgAndNumCheck(msg, num):
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
        """
        Genrates and tests Logfile.
        
        @param cm_dir : Path to the Commit Man Directory. 
        @param test   : True if in test mode.

        @return
        False if Logfile does not accept standard input.
 
        """
        cm_dir=os.path.join(dir_path, '.cm')
        if not test:
            with open(os.path.join(cm_dir,'log.db'), 'w') as f:
                pass
            try:
                con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                cur = con.cursor()
                cur.execute('''CREATE TABLE log (message text, number integer, datetime timestamp)''')
                cur.execute('''INSERT INTO log (message, number, datetime ) VALUES ('Created repo',0,datetime('now', 'localtime'))''')
                list_subfolders = [f.name for f in os.scandir(cm_dir) if f.is_dir() and f.name.isdigit()]
                for folder in list_subfolders:    
                    sql = '''INSERT INTO log (message, number, datetime ) VALUES(?,?,datetime('now', 'localtime'))'''
                    cur.execute(sql,["Reinit msg",int(folder),])
                con.commit()
                con.close()
            except Exception as e:
                print(f"Failed to Create log file due to : {e}")
            finally:
                if con:
                    con.close()
        else:
            try:
                con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                cur = con.cursor()
                cur.execute('''INSERT INTO log (message, number, datetime ) VALUES ('Created repo',-1,datetime('now', 'localtime'))''')
                cur.execute('''DELETE FROM log WHERE number=-1''')
                con.commit()
                con.close()
            except Exception:
                return False
            return True
    
    @staticmethod
    def display_log(dir_path):
        """
        Prints contents of the log file.
        
        @param dir_path : Path to the target directory. 

        """
        try:
            cm_dir=os.path.join(dir_path, '.cm')
            if os.path.exists(cm_dir):
                log_path = os.path.join(cm_dir,'log.db')
                if os.path.exists(log_path):
                    con = sqlite3.connect(log_path)
                    cur = con.cursor()
                    sqlite_select_query = """SELECT * from log"""
                    cur.execute(sqlite_select_query)
                    rows = cur.fetchall()
                    rows  = [list(row) for row in rows]
                    print('\n')
                    rows = [['Commit Message','Commit Number','Commit Datetime']] + [[' ',' ',' ']] + rows
                    for row in rows:
                        print(("{:<35}"*len(row)).format(*row))
                    con.close()
                    print('\n')
                else:
                    print('Could not find log file, reinitiate using cm reinit')
            else:
                print('Commit Man not initialized, initialize using cm init')
        except:
            raise