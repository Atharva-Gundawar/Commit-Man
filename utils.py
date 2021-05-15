import os
import difflib
import shutil 
import filecmp

"""

folder structure:
    ├── .cm
    ├── files and folders
    ├── -------||-------
    ├── -------||-------
    └── -------||-------

"""

def compare_trees(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
    """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not compare_trees(new_dir1, new_dir2):
            return False
    return True
 
def copytree(src, dst, symlinks=False, ignore=None):
    """
    Copy a directory tree to another location.

    @param src: source directory path
    @param dst: destination directory path

    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def get_commit_diff(cm_file_path,file_path):
    """
    Prints line by line diff for 2 versions of a file .

    @param cm_file_path: Old version of the file
    @param file_path: New version of the file

    """
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
            
def commit(dir_path,msg):
    """
    Commits latest version of the directory into a new dir 
    in the .cm folder  
    
    @format
    name => v[num]_[msg]
    commit number => num
    commit msg => msg

    @param cm_file_path: Old version of the file
    @param file_path: New version of the file

    """
    # Pass full paths for dir_path and cm_path
    cm_dir=os.path.join(dir_path,'.cm')
    if os.path.isdir(cm_dir):
        try:
            v_num = 0
            list_subfolders = [f.name for f in os.scandir(cm_dir) if f.is_dir()]
            for folder in list_subfolders:
                num = int(folder.split('_')[0][1:])
                v_num = num if v_num < num else v_num
            cm_folder_name = f'v{str(v_num + 1)}_{msg}'
            cm_folder_path = os.path.join(cm_dir, cm_folder_name)
            os.mkdir(cm_folder_path)
            copytree(dir_path, cm_folder_path)
        except Exception as e:
            raise Exception(f'Commit failed because of {e}')
    else:
        raise Exception('Commit Man not initialized')

    
def revert(code,dir_path,is_num=True,if_force=False):
    """
    Reverts to an old version

    @param code: Vesion number or msg
    @param dir_path: Path of the directory
    @param if_force: To force revert in case of non commited 
    @param is_num: Is True if code is num and False if code is msg

    """
    # Pass full paths for dir_path and cm_path
    cm_dir=os.path.join(dir_path,'.cm')
    if os.path.isdir(cm_dir):
        list_subfolders = [f.name for f in os.scandir(cm_dir) if f.is_dir()]
        v_num = 0
        for folder in list_subfolders:
            num = int(folder.split('_')[0][1:])
            v_num = num if v_num < num else v_num
        for folder in list_subfolders:
            if v_num == int(folder.split('_')[0][1:]):
                if compare_trees(dir_path,os.path.join(cm_dir, folder)) or if_force:                     
                    try:
                        if is_num:
                            for folder in list_subfolders:
                                if code == int(folder.split('_')[0][1:]):
                                    os.rmdir(dir_path)
                                    os.mkdir(dir_path)
                                    copytree(dir_path,os.path.join(cm_dir, folder))
                        else :
                            for folder in list_subfolders:
                                if code == int(folder.split('_')[1]):
                                    os.rmdir(dir_path)
                                    os.mkdir(dir_path)
                                    copytree(dir_path,os.path.join(cm_dir, folder))
                    except:
                        raise ValueError('Commit not found')
                else:
                    raise Exception('Latest code not commited')
            else:
                raise Exception('Latest version not found')
    else:
        raise Exception('Commit Man not initialized')

def init(dir_path):
    """
    Make .cm folder
    """
    try:
        os.mkdir(os.path.join(dir_path, '.cm'))
    except Exception as e:
        raise Exception('Initialization failed due to')

