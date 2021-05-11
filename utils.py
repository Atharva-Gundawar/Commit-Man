import os

def get_files(directory = os.curdir):
    files =[]
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files.append(os.path.join(path, name))
    return files