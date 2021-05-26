import os
from argparser import GetArgumentParser
from cmManager import CommitMan

def main():
    """
    Main function which handles argumenst passed,
    and calls respective functions. 

    """
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    cur_dir = os.path.abspath(os.path.curdir)
    cur_dir = '../test'
    if arguments['init']:
        CommitMan.init(cur_dir)
    elif arguments['commit']:
        CommitMan.commit(cur_dir,arguments['<message>'])
    elif arguments['revert']:
        CommitMan.revert(arguments['<number>'],cur_dir,arguments['--force'])
    elif arguments['reinit']:
        CommitMan.reinit(cur_dir)
    else:
        print(argparse.doc)


if __name__ == '__main__' :
    main()