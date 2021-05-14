import os
import difflib

def get_files(directory = os.curdir):
    files =[]
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files.append(os.path.join(path, name))
    return files

def get_commit_diff(cm_file_path,file_path):
    # cm_file_path is the path of the file saved inside the .cm folder.
    # file_path is the path of the file in the active directory.
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
            
"""
format of saving files will be in the follwoing manner
dir name => v[number]_[msg]
commit number => num
commit msg => msg
"""

def commit(dir_path,cm_dir,messgae):
    list_subfolders_with_paths = [f.path for f in os.scandir(dir_path) if f.is_dir()]
    print(list_subfolders_with_paths)

