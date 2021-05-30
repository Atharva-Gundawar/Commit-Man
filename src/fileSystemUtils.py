from gitignore_parser import parse_gitignore
import filecmp
import difflib
import shutil
import errno
import os
class FileUtils:
    """
    FileUtils class contains all the functions
    required to handle file operations
    
    @functions
    get_commit_diff => Returns diffrence of 2 versions of a file.
    compareTrees    => Compare two directories recursively.
    copyTree        => Copy a directory tree to another location.
    silentremove    => Deletes file
    rmtree          => Deletes folder recursively
    in_ignored      => Whether file is in gitignore 

    """
    @staticmethod
    def in_ignored(file_path,gitignore_path):
        """
        Ignores files and folders from the gitignore file.

        @param file_path: Name of the file.
        @param gitignore_path: Path to the gitignore file.

        @return: True if matches gitignore, else False.
        """
        if os.path.exists(gitignore_path):
            matches_gitignore = parse_gitignore(gitignore_path)
            return matches_gitignore(os.path.abspath(file_path))
        else:
            return False

    @staticmethod
    def get_commit_diff(cm_file_path,file_path):
        """
        Prints line by line diffrence for 2 versions of a file .

        @param cm_file_path: Old version of the file
        @param file_path: New version of the file

        @return file diffrence
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
                    file_diff.append(line)
        return file_diff

    @staticmethod
    def compareTrees(dir1, dir2, gitignore_path):
        """
        Compare two directories recursively. Files in each directory are
        assumed to be equal if their names and contents are equal.
        It ignores specified folders and files.

        @param dir1: First directory path
        @param dir2: Second directory path

        @return: True if the directory trees are the same and 
            there were no errors while accessing the directories or files, 
            False otherwise.
        """
        # Files that have to be ignores but are not in .gitignore

        ignore_folders_and_files = ['.git','.cm','.gitignore'] 
        dirs_cmp = filecmp.dircmp(dir1, dir2)
        for item in dirs_cmp.left_only:
            if item not in ignore_folders_and_files and not FileUtils.in_ignored(os.path.join(dir1,item),gitignore_path):
                return False
        if len(dirs_cmp.right_only)>0 or len(dirs_cmp.funny_files)>0:
            return False
        (_, mismatch, errors) =  filecmp.cmpfiles(
            dir1, dir2, dirs_cmp.common_files, shallow=False)
        if len(mismatch)>0 or len(errors)>0:
            print("mistakes: ",mismatch)
            print("errors: ",errors)
            return False
        for common_dir in dirs_cmp.common_dirs:
            new_dir1 = os.path.join(dir1, common_dir)
            new_dir2 = os.path.join(dir2, common_dir)
            if not FileUtils.compareTrees(new_dir1, new_dir2, gitignore_path):
                return False
        return True
    
    @staticmethod
    def copyTree(src, dst, gitignore_path, symlinks=False, ignore=None):
        """
        Copy a directory tree to another location.
        It ignores copying if .cm folder.

        @param src: source directory path
        @param dst: destination directory path

        """
        ignore_folders_and_files = ['.git','.cm','.gitignore'] 
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.basename(s) not in ignore_folders_and_files and not FileUtils.in_ignored(s,gitignore_path):
                if os.path.isdir(s):
                    if not os.path.isdir(d):
                        os.mkdir(d)
                    FileUtils.copyTree(s, d, gitignore_path, symlinks, ignore)
                else:
                    if not os.path.isfile(d):
                        with open(d,'w+') as f:
                            pass
                    shutil.copy2(s, d)
    
    @staticmethod
    def silentremove(file_path):
        """
        Deletes file if exists .

        @param filename : filename path

        """
        try:
            os.remove(file_path)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise 
    
    @staticmethod
    def rmtree(dir_path,gitignore_path):
        """
        Deletes all files and folders from a directory
        recursively while ignoreing the .cm and .git folder.
        
        @param dir_path: Path of the directory

        """
        full_dir_path = os.path.abspath(dir_path)
        ignore_folders_and_files = ['.git','.cm','.gitignore'] 
        for item in os.listdir(dir_path):
            if item not in ignore_folders_and_files and not FileUtils.in_ignored(os.path.join(dir_path,item),gitignore_path):
                if os.path.isdir(os.path.join(full_dir_path,item)):
                    full_item_path = os.path.join(full_dir_path,item)
                    shutil.rmtree(full_item_path)
                else:
                    FileUtils.silentremove(os.path.join(full_dir_path,item))
