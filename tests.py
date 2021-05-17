from utils import (log_format_check,msg_and_num_check,
                    update_logfile,compare_trees,
                    copytree,get_commit_diff,commit,
                    revert,init)
import os

dir_path = '.'
cm_dir = os.path.join(dir_path, '.cm')
log_file_path = os.path.join(cm_dir,'log.db')
msg = 'cm msg'
num = 234

dir1 = '.'
dir2 = '.'

src = '.'
dst = '.'

code = 234

def test_log_format_check():
    assert log_format_check(log_file_path) == 0 , "Error"


def test_msg_and_num_check():
    assert msg_and_num_check(msg, num) == 0 , "Error"


def test_update_logfile():
    assert update_logfile(cm_dir,msg,num) == 0 , "Error"


def test_compare_trees():
    assert compare_trees(dir1, dir2) == 0 , "Error"


def test_copytree():
    assert copytree(src, dst, symlinks=False, ignore=None) == 0 , "Error"


def test_commit():
    assert commit(dir_path,msg) == 0 , "Error"


def test_revert():
    assert revert(code,dir_path,is_num=True,if_force=False) == 0 , "Error"


def test_init():
    assert init(dir_path) == 0 , "Error"


if __name__ == "__main__":
    test_log_format_check()
    test_msg_and_num_check()
    test_update_logfile()
    test_compare_trees()
    test_copytree()
    test_commit()
    test_revert()
    test_init()
    print("Everything passed")