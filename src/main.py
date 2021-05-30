from src.argparser import GetArgumentParser
from src.logfileUtils import LogUtils
from src.cmManager import CommitMan
import sys
import os

commands = {
    'init' : """
Initialize Commit man in the current directory

Usage : cm init

This will create a .cm folder in the current directory,
and a log file inside that folder.
""",

    "reinit" : """
Reinitialize Commit man in the current directory

Usage : cm reinit

This will reinitialize .cm folder in case of
logfile corruption or unavailability.
""",
    
    "commit" : """
Commits curent version of working directory

Usage : cm commit <message>

This will create a new commit folder insider the .cm folder.
""",
    "revert" : """
Reverts to an old version of working directory

Usage : cm revert <Commit_Number> [-f | --force]

This revert to an older version of the project and with the 
force option revert will take place even if the latest code 
has not been commited.
""",
    "showlog" : """
Displays Log file in a tabular format on the Terminal

Usage : cm showlog

Queries data from the log file and adds headers and spacing,
then displays them to the terminal.

"""
}

def main():
    """
    Main function which handles argumenst passed,
    and calls respective functions. 

    """
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    cur_dir = os.path.abspath(os.path.curdir)
    if arguments['init']:
        CommitMan.init(cur_dir)
    elif arguments['commit']:
        CommitMan.commit(cur_dir,arguments['<message>'])
    elif arguments['revert']:
        CommitMan.revert(arguments['<number>'],cur_dir,arguments['--force'])
    elif arguments['reinit']:
        CommitMan.reinit(cur_dir)
    elif arguments['showlog']:
        LogUtils.display_log(cur_dir)
    elif arguments['man']:
        print("\n")
        print("#"*60)
        print('-'*60)
        for command in commands.keys():
            print(f'\n{command}:\n{commands[command]}')
            print('-'*60)
        print("#"*60,"\n")

    else:
        print(argparse.doc)


if __name__ == '__main__' :
    main()