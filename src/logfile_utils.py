class LogUtils:
    @staticmethod
    def msg_and_num_check(msg, num):
        """
        Checks Commit Message & Commit Number are in the correct format 
        
        @param msg: Commit Message
        @param num: Commit Number

        @return Commit Message & Commit Number are in the correct format
                else returns False

        """
        return(isinstance(msg, str) and isinstance(num,str)
            and len(msg) > 0 and len(msg) < 128
            and int(num) > 0
            and msg is not None and num is not None
            )
    
    @staticmethod
    def update_logfile(cm_dir,msg,num):
        """
        Updates log file with Commit Message, Commit Number and Datetime
        
        @param cm_dir : Path to the Commit Man Directory 
        @param msg: Commit Message
        @param num: Commit Number

        """

        if msg_and_num_check(msg, num):
            if os.path.exists(os.path.join(cm_dir,'log.db')):
                    try:
                        con = sqlite3.connect(os.path.join(cm_dir,'log.db'))
                        cur = con.cursor()
                        cur.execute(f'''INSERT INTO log (message, number, datetime ) VALUES({msg}, {num+1},datetime('now', 'localtime'))''')
                        con.commit()
                        con.close()
                    except Exception as e:
                        raise Exception(f'SQL database could not be updated : {e}')
            else:
                raise Exception('Cannot find log file')
        else:
            raise Exception('Check commit msg')
