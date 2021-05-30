from src.__init__ import __version__ as version
import sys

sys.dont_write_bytecode = True

from docopt import docopt

class GetArgumentParser:
   
    """
    Argument Parser class for Commit Man:
    
    @functions
    __init__     => Initializes docopt
    getArguments => Returns docopt
    
    """

    def __init__(self):
        """
        Initializes Usage of arguments for Docopt

        """
        doc = """Commit Man.

                Usage:
                    main.py init 
                    main.py commit <message>
                    main.py reinit
                    main.py revert <number> [-f | --force]
                    main.py man
                    main.py showlog
                    main.py (-h | --help)
                    main.py --version
                Options:
                    -h --help     Show this screen.
                    -f --force    Force
                    --version     Show version.

                """
        self.doc = doc
        self.version = version
        self.name = "Commit man"

    def getArguments(self):
        """
        Initializes Docopt.

        @return
        Docopt object for Argument Parsing 
        """
        return docopt(self.doc, version=f'{self.name}_{self.version}')


if __name__ == '__main__':
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    print(arguments)
