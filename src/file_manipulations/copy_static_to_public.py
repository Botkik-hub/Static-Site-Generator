import os
import shutil

def copy_static_to_public(copy_from, copy_to):
    if not os.path.exists(copy_to):
        os.mkdir(copy_to)
    if not os.path.exists(copy_from):
        raise Exception("Static directory does not exist")
    
    dir_objects = os.listdir(copy_from)
    for dir_object in dir_objects:
        path_from = os.path.join(copy_from, dir_object)
        path_to = os.path.join(copy_to, dir_object)
        if os.path.isfile(path_from):
            shutil.copy(path_from, path_to)
        else:
            if not os.path.exists(path_to):
                os.mkdir(path_to)
            copy_static_to_public(path_from, path_to)
