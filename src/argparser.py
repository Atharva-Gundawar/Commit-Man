import argparse

class GetArgumentParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Welcome to COMMIT MAN')
        parser.add_argument("-f", "--force",type=str,help="For Force mode")
        parser.add_argument("-p", "--path", type=str,help="Path to target directory")
        self.parser = parser

    def getParser(self):
        return self.parser