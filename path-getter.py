import os
import platform
import sys
from pathlib import Path

class Path_getter():
    def __init__(self):
        pass

    def get_path_directory(self, carpeta):
        #obtener el path del archivo 
        if platform.system() == 'Windows':
            #path = os.getcwd()
            path = Path.cwd()
            path = path + "\\" carpeta "\\"
            return path
        else:
            path = os.getcwd()
            #path = Path.cwd()
            #print(type(path))
            path = path + "/" animaciones "/"
            return path
    
    def get_path_archive(self, carpeta, archive):
        #obtener el path del archivo 
        if platform.system() == 'Windows':
            #path = os.getcwd()
            path = Path.cwd()
            path = path + "\\" carpeta "\\" + archive
            return path
        else:
            path = os.getcwd()
            #path = Path.cwd()
            #print(type(path))
            path = path + "/" animaciones "/" + archive
            return path
    

