from shutil import rmtree
from os import listdir, mkdir
from os.path import join, isfile, isdir, exists


def make_dir_helper(dir_path):
    if not exists(dir_path):
        mkdir(dir_path)
        return True
    return False


def delete_dir_helper(dir_path):
    if exists(dir_path):
        rmtree(dir_path)
        return True
    return False


def is_jpeg(fname):
    return fname.split('.')[-1] == 'jpg'
