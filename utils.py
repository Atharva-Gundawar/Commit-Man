import os
import difflib
import shutil 

"""
format of saving files will be in the follwoing manner
dir name => v[num]_[msg]
commit number => num
commit msg => msg
"""

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def get_files(directory=os.curdir):
    files = []
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
            
def commit(dir_path,cm_dir,msg):
    # Pass full paths for dir_path and cm_path
    v_num = 0
    list_subfolders = [f.name for f in os.scandir(cm_dir) if f.is_dir()]
    for folder in list_subfolders:
        num = int(folder.split('_')[0][1:])
        v_num = num if v_num < num else v_num
    cm_folder_name = f'v{str(v_num + 1)}_{msg}'
    cm_folder_path = os.path.join(cm_dir, cm_folder_name)
    os.mkdir(cm_folder_path)
    copytree(dir_path,cm_folder_path)
    
def revert(code,dir_path,cm_dir,is_num=True):
    list_subfolders = [f.name for f in os.scandir(cm_dir) if f.is_dir()]
    if is_num:
        try:
            for folder in list_subfolders:
                if code == int(folder.split('_')[0][1:]):
                    os.rmdir(dir_path)
                    os.mkdir(dir_path)
                    copytree(dir_path,os.path.join(cm_dir, folder))            
        except :
            raise ValueError('Commit not found')
    else:
        try:
            for folder in list_subfolders:
                if code == int(folder.split('_')[1]):
                    os.rmdir(dir_path)
                    os.mkdir(dir_path)
                    copytree(dir_path,os.path.join(cm_dir, folder))
        except :
            raise ValueError('Commit not found')