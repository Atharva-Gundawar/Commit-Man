# Command descriptions for Commit Man
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