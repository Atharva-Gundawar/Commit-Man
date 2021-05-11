import os
import difflib

def get_files(directory = os.curdir):
    files =[]
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files.append(os.path.join(path, name))
    return files

def get_commit_diff(cm_file_path,file_path):
    file_diff = []
    with open(cm_file_path, 'r') as hosts0:
        with open(file_path, 'r') as hosts1:
            diff = difflib.unified_diff(
                hosts0.readlines(),
                hosts1.readlines(),
                fromfile='old',
                tofile='new',
            )
            for line in diff:
                file_diff(line)