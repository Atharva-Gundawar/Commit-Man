import os
from argparser import GetArgumentParser
from cmManager import CommitMan

def main():
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    cur_dir = os.path.abspath(os.path.curdir)
    if arguments['cm']:
        if arguments['init']:
            CommitMan.init(cur_dir)
        elif arguments['commit']:
            CommitMan.commit(cur_dir,arguments['<message>'])
        elif arguments['revert']:
            CommitMan.revert(arguments['<number>'],cur_dir,arguments['--force'])
        else:
            print(argparse.doc)
    else:
        print(argparse.doc)

if __name__ == '__main__' :
    main()