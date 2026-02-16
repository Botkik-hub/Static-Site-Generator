from file_manipulations.generate_page import *

import os

def convert_directory(copy_from, copy_to, template_path, basepath):
    if not os.path.exists(copy_to):
        os.mkdir(copy_to)
    if not os.path.exists(copy_from):
        raise Exception("Static directory does not exist")
    
    dir_objects = os.listdir(copy_from)
    for dir_object in dir_objects:
        path_from = os.path.join(copy_from, dir_object)
        path_to = os.path.join(copy_to, dir_object.replace(".md", ".html"))
        if os.path.isfile(path_from):
            generate_page(path_from, template_path, path_to, basepath)
        else:
            if not os.path.exists(path_to):
                os.mkdir(path_to)
            convert_directory(path_from, path_to, template_path, basepath)
