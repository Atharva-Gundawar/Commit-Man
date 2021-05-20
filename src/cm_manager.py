import os
import difflib
import shutil 
import filecmp
import pytz    
import datetime
import csv   
import sys
import sqlite3

"""
Folder structure:
    ├── .cm
    │   ├── log.db
    │   ├── Commit Folder
    │   ├── Commit Folder
    │   └── Commit Folder
    │
    ├── files and folders
    ├── -------||-------
    ├── -------||-------
    └── -------||-------


@Commit_Folder_Naming_Scheme
    name => [num]
    commit number => num
    commit msg => msg

Log file structure:
    message -> TEXT,
    number -> INT,
    datetime -> TIMESTAMP

"""

class Commit_man:

    @staticmethod
    def init(dir_path):
        """
        Make .cm folder and log file

        @param dir_path: Path to directory 
        """
        try:
            if os.path.exists(os.path.join(dir_path, '.cm')):
                sys.exit('Commit man already initialized for this directory')
            os.mkdir(os.path.join(dir_path, '.cm'))
            fields=['Commit Number', 'Commit message', 'Datetime']
            with open(os.path.join(os.path.join(dir_path, '.cm'),'log.db'), 'w') as f:
                pass
            try:
                con = sqlite3.connect(os.path.join(os.path.join(dir_path, '.cm'),'log.db'))
                cur = con.cursor()
                cur.execute('''CREATE TABLE log
                    (message text, number integer, datetime timestamp)''')
                cur.execute('''INSERT INTO log (message, number, datetime )
                        VALUES('Created repo',0,datetime('now', 'localtime'))''')
                con.close()
            except Exception as e:
                print("Failed to Create log file", e)
            finally:
                if con:
                    con.close()
        except Exception as e:
            raise Exception(f'Initialization failed due to {e}')


    @staticmethod
    def commit(dir_path,msg):
        """
        Commits latest version of the directory into a new dir 
        in the .cm folder and updates log file. 
        
        @format
        name => num
        commit number => num
        commit msg => msg

        @param dir_path: Path of the directory
        @param msg: Commit msg 

        """
        cm_dir=os.path.join(dir_path,'.cm')
        if os.path.isdir(cm_dir):
            if os.path.exists(os.path.join(cm_dir,'log.db')):

                try:
                    con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                    cur = con.cursor()
                    sqlite_select_query = """SELECT MAX(number) from log"""
                    cur.execute(sqlite_select_query)
                    v_num = cur.fetchall()[0][0]
                    con.close()

                    if v_num:
                        update_logfile(cm_dir,msg,v_num)
                    else:
                        raise Exception('Log file corrupted, reinitiate using cm reinit')

                except Exception as e:
                    raise Exception(f'Log file not updated because of {e}')
            
            else:
                raise Exception('Log file not found, reinitialize using cm reinit')

            try:
                cm_folder_name = f'{v_num + 1}'
                cm_folder_path = os.path.join(cm_dir, cm_folder_name)
                os.mkdir(cm_folder_path)
                copytree(dir_path, cm_folder_path)
            except Exception as e:
                print('Last commit failed , trying to delete from logs')

                try:
                    con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                    cur = con.cursor()
                    sqlite_select_query = f"""DELETE FROM log WHERE number={v_num};"""
                    cur.execute(sqlite_select_query)
                    con.close()
                except Exception as e:
                    raise Exception(f'Log file deletion failed because of {e}')

                raise Exception(f'Commit failed because of {e}')
        else:
            raise Exception('Commit Man not initialized')
    
    @staticmethod   
    def revert(num,dir_path,if_force=False):
        """
        Reverts to an old version

        @param num: Vesion number
        @param dir_path: Path of the directory
        @param if_force: To force revert in case of non commited 

        """
        cm_dir=os.path.join(dir_path,'.cm')
        if os.path.isdir(cm_dir):
            list_subfolders = [f.name for f in os.scandir(cm_dir) if f.is_dir()]
            v_num = 0
            try:
                con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                cur = con.cursor()
                sqlite_select_query = """SELECT MAX(number) from log"""
                cur.execute(sqlite_select_query)
                big_num = cur.fetchall()[0][0]
                con.close()

                if big_num:
                    v_num = big_num
                else:
                    raise Exception('Revert Failed, Log file corrupted, reinitiate using cm reinit ')

            except Exception as e:
                raise Exception(e)
            
            if str(v_num) in list_subfolders:
                for folder in list_subfolders:
                    if str(v_num) == folder:
                        if compare_trees(dir_path,os.path.join(cm_dir, folder)) or if_force:                     
                            try:
                                os.rmdir(dir_path)
                                os.mkdir(dir_path)
                                copytree(dir_path,os.path.join(cm_dir, folder))
                            except Exception as e:
                                raise Exception(f'Revert failed due to {e}')
                        else:
                            raise Exception('Latest code not commited')
                    else:
                        pass
            else:
                raise Exception(f'Commit {v_num} not found')
        else:
            raise Exception('Commit Man not initialized')
