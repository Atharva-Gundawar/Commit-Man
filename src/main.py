from src.argparser import GetArgumentParser
from src.logfileUtils import LogUtils
from src.cmManager import CommitMan
import src.manPages 
import sys
import os

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
        for command in manPages.commands.keys():
            print(f'\n{command}:\n{manPages.commands[command]}')
            print('-'*60)
        print("#"*60,"\n")

    else:
        print(argparse.doc)


if __name__ == '__main__' :
    main()