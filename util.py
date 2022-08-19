import time
import os
import shutil

def create_dirs(dir):
    # if directory already exist then remove them completely and create new Directories
    # directories for storing temporary edited images and pdf to image files
    if(os.path.isdir(dir)):
        shutil.rmtree(dir)
    os.mkdir(dir)

def rm_dir(dir):
    if(os.path.isdir(dir)):
        shutil.rmtree(dir)
        
def get_time():
    return time.time()

def print_gap(x):
    for i in range(x):
        print()
    return