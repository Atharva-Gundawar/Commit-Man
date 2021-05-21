from __init__ import __version__ as version
# import argparse

# class GetArgumentParser:
#     def __init__(self):
#         parser = argparse.ArgumentParser(description='Welcome to COMMIT MAN')
#         parser.add_argument("-f", "--force",type=str,help="For Force mode")
#         parser.add_argument("-p", "--path", type=str,help="Path to target directory")
#         self.parser = parser

#     def getParser(self):
#         return self.parser

from docopt import docopt

class GetArgumentParser:
    def __init__(self):
        doc = """Commit Man.

                Usage:
                    main.py cm init 
                    main.py cm commit [-f | --force]
                    main.py cm revert [-f | --force]
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
        return docopt(self.doc, version=f'{self.name}_{self.version}')


if __name__ == '__main__':
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    print(arguments)
