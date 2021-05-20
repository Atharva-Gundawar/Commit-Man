class File_utils:
    
    @staticmethod
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
    
    @staticmethod
    def copytree(src, dst, symlinks=False, ignore=None):
        """
        Copy a directory tree to another location.
        It ignores copying if .cm folder is found
        in its path

        @param src: source directory path
        @param dst: destination directory path

        """
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s) and '.cm' not in s:
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    @staticmethod
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
                